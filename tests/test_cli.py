"""Subprocess tests for the ``aso`` CLI."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent
FIXTURES = REPO_ROOT / "tests" / "fixtures"


def _run(args, stdin: str = "", env_extra=None):
    env = None
    if env_extra:
        import os

        env = {**os.environ, **env_extra}
    return subprocess.run(
        [sys.executable, "-m", "aso_skill", *args],
        input=stdin,
        capture_output=True,
        text=True,
        cwd=REPO_ROOT,
        env=env,
    )


def test_help_returns_zero():
    proc = _run(["--help"])
    assert proc.returncode == 0
    assert "score" in proc.stdout
    assert "validate" in proc.stdout


def test_version_returns_zero():
    proc = _run(["--version"])
    assert proc.returncode == 0
    assert "aso" in proc.stdout.lower()


def test_validate_valid_title_returns_zero():
    proc = _run(["validate", "--platform", "apple", "--field", "title", "--value", "TaskFlow"])
    assert proc.returncode == 0


def test_validate_invalid_title_returns_one():
    proc = _run(
        [
            "validate",
            "--platform",
            "apple",
            "--field",
            "title",
            "--value",
            "X" * 50,
        ]
    )
    assert proc.returncode == 1


def test_score_subcommand_from_fixture():
    fixture = (FIXTURES / "score_input.json").read_text()
    proc = _run(["score"], stdin=fixture)
    assert proc.returncode == 0, proc.stderr
    payload = json.loads(proc.stdout)
    assert 0 <= payload["overall_score"] <= 100


def test_keywords_subcommand_from_fixture():
    fixture = (FIXTURES / "keywords_input.json").read_text()
    proc = _run(["keywords"], stdin=fixture)
    assert proc.returncode == 0, proc.stderr
    payload = json.loads(proc.stdout)
    assert isinstance(payload, dict)


def test_legacy_script_path_still_works():
    """The agent contract: ``python3 aso_scorer.py < input.json``.

    Before this PR, the module had no ``__main__`` block — the call was broken.
    """
    fixture = (FIXTURES / "score_input.json").read_text()
    proc = subprocess.run(
        [sys.executable, "app-store-optimization/aso_scorer.py"],
        input=fixture,
        capture_output=True,
        text=True,
        cwd=REPO_ROOT,
    )
    assert proc.returncode == 0, proc.stderr
    payload = json.loads(proc.stdout)
    assert "overall_score" in payload
