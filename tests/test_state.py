"""Tests for the per-app StateStore."""

from __future__ import annotations

import json

import pytest

from aso_skill.state import CURRENT_SCHEMA_VERSION, StateStore


def test_load_returns_empty_state_when_no_file(tmp_path):
    store = StateStore("TestApp", base_dir=tmp_path)
    state = store.load()
    assert state["schema_version"] == CURRENT_SCHEMA_VERSION
    assert state["app_name"] == "TestApp"
    assert state["apple_metadata"] is None


def test_save_creates_file_with_atomic_path(tmp_path):
    store = StateStore("TestApp", base_dir=tmp_path)
    path = store.save({"apple_metadata": {"title": "TaskFlow"}})
    assert path == tmp_path / "TestApp" / ".state" / "current.json"
    assert path.is_file()
    data = json.loads(path.read_text())
    assert data["apple_metadata"] == {"title": "TaskFlow"}
    assert data["last_updated"] is not None


def test_save_stamps_schema_version_and_app_name(tmp_path):
    store = StateStore("TestApp", base_dir=tmp_path)
    store.save({"apple_metadata": {}, "schema_version": 999, "app_name": "wrong"})
    state = store.load()
    assert state["schema_version"] == CURRENT_SCHEMA_VERSION
    assert state["app_name"] == "TestApp"


def test_round_trip_preserves_payload(tmp_path):
    store = StateStore("TestApp", base_dir=tmp_path)
    payload = {
        "apple_metadata": {"title": "Tasks", "subtitle": "for everyone"},
        "google_metadata": {"title": "Tasks for everyone"},
        "keyword_set": ["task", "todo", "productivity"],
        "last_aso_score": 78.5,
        "competitors": [{"name": "Todoist", "rating": 4.8}],
    }
    store.save(payload)
    loaded = store.load()
    for key, value in payload.items():
        assert loaded[key] == value


def test_update_merges_one_slot_without_clobbering_others(tmp_path):
    store = StateStore("TestApp", base_dir=tmp_path)
    store.save({"apple_metadata": {"title": "Tasks"}, "last_aso_score": 80.0})
    store.update(last_aso_score=85.0)
    state = store.load()
    assert state["last_aso_score"] == 85.0
    assert state["apple_metadata"] == {"title": "Tasks"}


def test_update_rejects_unknown_slots(tmp_path):
    store = StateStore("TestApp", base_dir=tmp_path)
    with pytest.raises(ValueError, match="unknown state slot"):
        store.update(launched_at="2026-01-01")


def test_empty_app_name_rejected():
    with pytest.raises(ValueError):
        StateStore("")
    with pytest.raises(ValueError):
        StateStore("   ")


def test_future_schema_version_raises(tmp_path):
    store = StateStore("TestApp", base_dir=tmp_path)
    store.state_dir.mkdir(parents=True, exist_ok=True)
    store.path.write_text(
        json.dumps({"schema_version": CURRENT_SCHEMA_VERSION + 99, "app_name": "TestApp"})
    )
    with pytest.raises(ValueError, match="newer than this code"):
        store.load()


def test_atomic_write_leaves_no_temp_files(tmp_path):
    store = StateStore("TestApp", base_dir=tmp_path)
    store.save({"apple_metadata": {"title": "Tasks"}})
    leftover = list(store.state_dir.glob("current.*.json.tmp"))
    assert leftover == []


def test_exists_reflects_disk_state(tmp_path):
    store = StateStore("TestApp", base_dir=tmp_path)
    assert store.exists() is False
    store.save({"apple_metadata": {}})
    assert store.exists() is True
