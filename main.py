#!/usr/bin/env python3
"""One office joke, written to /output/entry.txt and printed to stdout.

The entry is exactly one joke, nothing else: no title, no explanation,
no trailing newline.
"""

import os
import sys

ENTRY = "My boss asked me to open the meeting with a joke, so I put his salary on the first slide."

MAX_CHARS = 200


def main() -> None:
    if not 1 <= len(ENTRY) <= MAX_CHARS:
        raise ValueError(f"entry must be 1-{MAX_CHARS} characters, got {len(ENTRY)}")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    sys.stdout.write(ENTRY)


if __name__ == "__main__":
    main()
