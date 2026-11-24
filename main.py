#!/usr/bin/env python3
"""One-line cat joke entry for make.fun.

Writes a single cat joke, one line under 200 characters, to
/output/entry.txt. Standard library only.
"""

import os

ENTRY = "My cat knocked my phone off the counter, looked me dead in the eye, and purred — that wasn't an accident, it was a performance review."


def main():
    # The gate: /output/entry.txt must be 1-200 characters, not only whitespace.
    assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars"
    assert ENTRY.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
