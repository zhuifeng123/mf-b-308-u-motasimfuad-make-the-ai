#!/usr/bin/env python3
"""Write the competition entry to /output/entry.txt (deterministic, stdlib only)."""

import os

ENTRY = (
    "Still hasn't figured out that I want the same food every day after nine "
    "years. One star."
)

OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def main() -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")
    assert "\n" not in ENTRY, "entry must be a single line"
    assert len(ENTRY) < 200, f"entry too long: {len(ENTRY)} chars"


if __name__ == "__main__":
    main()
