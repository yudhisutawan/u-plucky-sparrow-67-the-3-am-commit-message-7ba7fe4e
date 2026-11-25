#!/usr/bin/env python3
"""The 3 AM Commit Message — make.fun entry.

Writes the winning one-line commit message to $MAKEFUN_OUTPUT_DIR/entry.txt
(or /output/entry.txt when the variable is unset).

The entry text is exactly 105 characters (winner R4b); the length guard below
protects that invariant — the output must not change.
"""

import os

ENTRY = "fix: I am so sorry, I panicked at 3am and wrote a postmortem blaming a junior engineer who does not exist"
assert len(ENTRY) == 105, f"entry must be 105 chars, got {len(ENTRY)}"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
