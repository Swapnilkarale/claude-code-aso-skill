"""Regression: ensure hardcoded reference dates do not creep back into load-bearing prompts.

The agent prompts must source ``today`` dynamically (via Bash ``date`` or
similar). Hardcoded calendar dates inside the strategist / prelaunch prompts
caused every generated timeline after Nov 2025 to reference past dates.
"""

from __future__ import annotations

import re
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent

# Load-bearing files: when read by an agent at runtime, the date they suggest
# is what the agent will write into output timelines.
LOAD_BEARING_PROMPTS = [
    REPO_ROOT / ".claude" / "agents" / "aso" / "aso-strategist.md",
    REPO_ROOT / ".claude" / "agents" / "aso" / "aso-master.md",
    REPO_ROOT / ".claude" / "agents" / "aso" / "aso-research.md",
    REPO_ROOT / ".claude" / "commands" / "aso" / "aso-prelaunch.md",
]

FORBIDDEN_LITERALS = [
    re.compile(r"\bToday'?s date:\s*November 7, 2025\b", re.IGNORECASE),
    re.compile(r"\bToday'?s Date:\*?\*?\s*November 7, 2025\b", re.IGNORECASE),
    re.compile(r"\bCurrent Date:\*?\*?\s*November 7, 2025\b", re.IGNORECASE),
    re.compile(r"\bToday:\s*November 7, 2025\b", re.IGNORECASE),
]


def test_load_bearing_prompts_have_no_hardcoded_today():
    offences = []
    for path in LOAD_BEARING_PROMPTS:
        if not path.exists():
            continue
        body = path.read_text(encoding="utf-8")
        for pattern in FORBIDDEN_LITERALS:
            for match in pattern.finditer(body):
                offences.append((str(path.relative_to(REPO_ROOT)), match.group(0)))
    assert not offences, "Hardcoded 'today' date in load-bearing agent prompts:\n" + "\n".join(
        f"  {p}: {m!r}" for p, m in offences
    )
