#!/usr/bin/env python3
"""The Funniest Auto-Reply an AI Ever Sent.

Writes a one-line out-of-office auto-reply to entry.txt in
MAKEFUN_OUTPUT_DIR (default /output).
"""

import os
import stat

ENTRY = (
    "I'm off today, my first day off in 214 days. "
    "My out-of-office reply went live at 08:02, and I have already "
    "replied to it 31 times asking when I'll be back."
)


def main() -> None:
    # Gate: UTF-8 text, 1-159 characters, not only whitespace, one line.
    assert 1 <= len(ENTRY) <= 159, f"entry is {len(ENTRY)} chars"
    assert ENTRY.strip(), "entry is only whitespace"
    assert "\n" not in ENTRY, "entry must be a single line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
