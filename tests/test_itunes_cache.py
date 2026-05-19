"""Tests for the iTunes file-cache wrapper. No network."""

from __future__ import annotations

import json
import time
from unittest.mock import patch

import pytest

from aso_skill.itunes_cache import ITunesCache, cached_urlopen


@pytest.fixture(autouse=True)
def _isolated_cache_dir(tmp_path, monkeypatch):
    """Each test gets a fresh cache dir + no bypass env var."""
    monkeypatch.delenv("ASO_ITUNES_NO_CACHE", raising=False)
    monkeypatch.delenv("ASO_ITUNES_TTL_SECONDS", raising=False)
    monkeypatch.setenv("XDG_CACHE_HOME", str(tmp_path))
    # Reset module-level global so it picks up the new dir
    import aso_skill.itunes_cache as ic

    monkeypatch.setattr(ic, "_GLOBAL_CACHE", None)
    yield tmp_path


def _fake_urlopen_factory(payload: dict):
    """Build a stub urlopen that returns ``payload`` as a JSON response."""
    calls = {"count": 0}

    class _FakeResponse:
        def __init__(self, data):
            self._data = data

        def read(self):
            return json.dumps(self._data).encode("utf-8")

        def __enter__(self):
            return self

        def __exit__(self, *a):
            return False

    def fake(url, timeout=10.0):
        calls["count"] += 1
        return _FakeResponse(payload)

    return fake, calls


def test_first_call_fetches_second_call_hits_cache():
    fake, calls = _fake_urlopen_factory({"resultCount": 1, "results": [{"trackName": "Hi"}]})
    with patch("aso_skill.itunes_cache.urllib.request.urlopen", side_effect=fake):
        first = cached_urlopen("https://example.com/foo")
        second = cached_urlopen("https://example.com/foo")
    assert first == second
    assert calls["count"] == 1, "second call should be served from cache"


def test_bypass_via_env_var(monkeypatch):
    monkeypatch.setenv("ASO_ITUNES_NO_CACHE", "1")
    fake, calls = _fake_urlopen_factory({"resultCount": 1, "results": []})
    with patch("aso_skill.itunes_cache.urllib.request.urlopen", side_effect=fake):
        cached_urlopen("https://example.com/foo")
        cached_urlopen("https://example.com/foo")
    assert calls["count"] == 2, "bypass should re-fetch every time"


def test_expired_entry_refetches(monkeypatch):
    monkeypatch.setenv("ASO_ITUNES_TTL_SECONDS", "1")
    fake, calls = _fake_urlopen_factory({"resultCount": 1, "results": []})
    with patch("aso_skill.itunes_cache.urllib.request.urlopen", side_effect=fake):
        cached_urlopen("https://example.com/foo")
        time.sleep(1.1)
        cached_urlopen("https://example.com/foo")
    assert calls["count"] == 2


def test_clear_removes_entries():
    fake, _ = _fake_urlopen_factory({"resultCount": 0, "results": []})
    with patch("aso_skill.itunes_cache.urllib.request.urlopen", side_effect=fake):
        cached_urlopen("https://example.com/a")
        cached_urlopen("https://example.com/b")
    removed = ITunesCache().clear()
    assert removed >= 2


def test_network_failure_falls_back_to_stale_cache(monkeypatch):
    """If the API is down and we have a stale entry, return it rather than fail hard."""
    fake_ok, _ = _fake_urlopen_factory({"resultCount": 1, "results": [{"ok": True}]})
    monkeypatch.setenv("ASO_ITUNES_TTL_SECONDS", "1")
    with patch("aso_skill.itunes_cache.urllib.request.urlopen", side_effect=fake_ok):
        first = cached_urlopen("https://example.com/foo")
    time.sleep(1.1)  # entry now expired

    import urllib.error

    def fake_fail(url, timeout=10.0):
        raise urllib.error.URLError("simulated outage")

    with patch("aso_skill.itunes_cache.urllib.request.urlopen", side_effect=fake_fail):
        fallback = cached_urlopen("https://example.com/foo")
    assert fallback == first, "should serve stale cache on network failure"
