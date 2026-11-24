#!/usr/bin/env python3
"""Write one short text for make.fun bounty u-ronigrv-a-day-of-one-line-pitches-12cd9bb3."""

from __future__ import annotations

import os
import sys
from pathlib import Path

TEXT = "My sister, who has never written code, sent make.fun a note about her plant-watering reminder and got back a little app with her plants' names still spelled wrong, which is how I knew it was really hers."

assert 1 <= len(TEXT) <= 280, f"text must be 1-280 characters, got {len(TEXT)}"


def output_dir() -> Path:
    """Folder named by MAKEFUN_OUTPUT_DIR when set, else OUTPUT_DIR, else /output."""
    for name in ("MAKEFUN_OUTPUT_DIR", "OUTPUT_DIR"):
        named = os.environ.get(name)
        if named:
            return Path(named)
    return Path("/output")


def main() -> int:
    target = output_dir()
    target.mkdir(parents=True, exist_ok=True)
    entry = target / "entry.txt"
    entry.write_bytes(TEXT.encode("utf-8"))
    print(len(TEXT), file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
