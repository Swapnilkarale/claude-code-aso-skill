"""Shared fixtures for the ASO test suite."""

from __future__ import annotations

import sys
from pathlib import Path

# Make the package importable from a source checkout without `pip install -e .`.
_REPO_ROOT = Path(__file__).resolve().parent.parent
if str(_REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(_REPO_ROOT))
