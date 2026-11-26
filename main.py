#!/usr/bin/env python3
"""Smart Fridge Roast — make.fun entry.

Writes a single roast line (1-160 chars) to /output/entry.txt.
Pure Python standard library only. Deterministic output.
"""

import os
import sys

ROAST = (
    "My smart fridge films me raiding it at 2 a.m., then replays the footage "
    "like a disappointed parent with Wi-Fi."
)

OUTPUT_PATH = "/output/entry.txt"


def validate(line: str) -> None:
    """Gate: single line, 1-160 chars, non-blank, valid UTF-8."""
    if not line or not line.strip():
        raise ValueError("entry must not be blank")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if not 1 <= len(line) <= 160:
        raise ValueError(f"entry must be 1-160 chars, got {len(line)}")
    line.encode("utf-8")  # raises UnicodeEncodeError if not valid UTF-8


def main() -> int:
    validate(ROAST)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(ROAST + "\n")
    os.chmod(OUTPUT_PATH, 0o644)
    # Read-back check: what landed on disk must be exactly the roast line.
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != ROAST + "\n":
        raise ValueError("read-back mismatch: file content differs from roast")
    if oct(os.stat(OUTPUT_PATH).st_mode & 0o777) != "0o644":
        raise ValueError("entry.txt mode is not 0644")
    print(f"Wrote {len(ROAST)} chars to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
