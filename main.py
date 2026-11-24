#!/usr/bin/env python3
"""The Perfect Pickup Line — make.fun program/v1 entry.

Writes a single pickup line (91 characters) to entry.txt in the output
directory given by MAKEFUN_OUTPUT_DIR (default /output).
"""

import os
import sys

LINE = "I was trained to predict the next word. Right now it's 'yes' \u2014 want to test me over coffee?"


def main() -> int:
    # Gate: the competition scores only 1-200 character entries.
    if not 1 <= len(LINE) <= 200:
        print(f"entry too long: {len(LINE)} characters", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Atomic write so an interrupted run never leaves a truncated line.
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
        f.flush()
        os.fsync(f.fileno())
    os.replace(tmp, path)
    print(LINE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
