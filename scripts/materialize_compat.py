"""Replace backward-compat symlinks with real file copies.

Use this on platforms that don't support symlinks (some Windows clones,
zip-extracted skills, archive uploads). After running, the legacy paths
under ``app-store-optimization/`` and ``.claude/skills/aso/`` become
regular files / directories with copies of the canonical source.

Usage:
    python3 scripts/materialize_compat.py [--repo-root <path>] [--dry-run]
"""

from __future__ import annotations

import argparse
import os
import shutil
import sys
from pathlib import Path
from typing import List


def _materialize(path: Path, dry_run: bool) -> bool:
    if not path.is_symlink():
        return False
    target = path.resolve()
    if not target.exists():
        # os.readlink works on Python 3.8; Path.readlink is 3.9+.
        sys.stderr.write(f"  skip (broken link): {path} -> {os.readlink(str(path))}\n")
        return False
    if dry_run:
        sys.stdout.write(f"  would materialize: {path} -> {target}\n")
        return True
    path.unlink()
    if target.is_dir():
        shutil.copytree(target, path, symlinks=False)
    else:
        shutil.copy2(target, path)
    sys.stdout.write(f"  materialized: {path}\n")
    return True


def _walk_and_materialize(root: Path, dry_run: bool) -> int:
    count = 0
    if root.is_symlink():
        if _materialize(root, dry_run):
            count += 1
        return count
    if not root.exists():
        return 0
    for entry in root.rglob("*"):
        if entry.is_symlink():
            if _materialize(entry, dry_run):
                count += 1
    return count


def main(argv: List[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", type=Path, default=Path(__file__).resolve().parent.parent)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args(argv)

    targets = [
        args.repo_root / "app-store-optimization",
        args.repo_root / ".claude" / "skills" / "aso",
    ]

    total = 0
    for target in targets:
        sys.stdout.write(f"Scanning {target.relative_to(args.repo_root)}\n")
        total += _walk_and_materialize(target, args.dry_run)
    verb = "would materialize" if args.dry_run else "materialized"
    sys.stdout.write(f"Done: {verb} {total} symlink(s).\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
