#!/usr/bin/env python3
"""One-Line Roast: The Gadget You Use Every Day.

Writes one original roast line to /output/entry.txt and verifies it
by reading it back: 1-200 characters, a single line, non-blank, ASCII.
"""

import os
import sys

LINE = (
    "My car beeps at a leaf, a shadow, and its own reflection, "
    "but stays silent for the one pole I actually hit."
)

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def main() -> int:
    parent = os.path.dirname(OUTPUT_PATH)
    if parent:
        os.makedirs(parent, exist_ok=True)

    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)

    # Verify by reading it back: the file must hold exactly the line
    # we intended, byte for byte, with no added whitespace or newline.
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as f:
        written = f.read()

    if written != LINE:
        print("error: read-back differs from the intended line", file=sys.stderr)
        return 1
    if written != written.strip():
        print("error: entry has leading or trailing whitespace", file=sys.stderr)
        return 1
    if not 1 <= len(written) <= 200:
        print(f"error: entry is {len(written)} chars, must be 1-200", file=sys.stderr)
        return 1
    if "\n" in written or "\r" in written:
        print("error: entry must be a single line", file=sys.stderr)
        return 1
    if not all(ord(c) < 128 for c in written):
        print("error: entry must be plain ASCII", file=sys.stderr)
        return 1

    print(f"wrote {len(written)} chars to {OUTPUT_PATH}")
    print(written)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
