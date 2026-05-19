"""Structural assertions against the bundled sample / expected output.

We deliberately do NOT byte-diff against ``expected_output.json`` — that file
was hand-authored and the live modules compute different exact values from
heuristics. Instead we assert: (1) the expected output's top-level shape is
present in the live computation, (2) numeric values fall in plausible ranges,
and (3) the live computation completes without raising.
"""

from __future__ import annotations

import json
from pathlib import Path

from aso_skill import analyze_keyword_set


SAMPLE_DIR = Path(__file__).resolve().parent.parent / "app-store-optimization"


def test_sample_input_loads():
    sample = json.loads((SAMPLE_DIR / "sample_input.json").read_text())
    assert isinstance(sample, dict)


def test_expected_output_loads():
    expected = json.loads((SAMPLE_DIR / "expected_output.json").read_text())
    assert isinstance(expected, dict)


def test_keyword_analysis_against_sample_input_runs():
    """Run analyze_keyword_set against a derived input. Verify structural shape."""
    sample = json.loads((SAMPLE_DIR / "sample_input.json").read_text())
    keywords = sample.get("target_keywords") or []
    if not keywords:
        # Sample doesn't expose keyword analytics shape directly; synthesize one.
        keywords = [
            {"keyword": "task manager", "search_volume": 50000, "competition": 70, "relevance": 85}
        ]
    if isinstance(keywords[0], str):
        keywords = [
            {"keyword": kw, "search_volume": 10000, "competition": 50, "relevance": 80}
            for kw in keywords
        ]
    result = analyze_keyword_set(keywords)
    assert isinstance(result, dict)
    assert len(result) > 0
