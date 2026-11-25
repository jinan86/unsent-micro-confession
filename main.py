#!/usr/bin/env python3
"""Unsent: The Micro-Confession Sprint.

Writes one two-part micro-confession to /output/entry.txt:
a "To:" line naming who the message was meant for, then the unsent
message itself on a single line, exactly as it was typed.

The confession is addressed to the night guard at the writer's old
building: six years of "good morning", a name never learned, and a
chair found empty the one morning the writer finally wanted to ask.
Too late is the reason it stayed in drafts, and it is felt in the
words rather than stated. Swapping the addressee would break it:
the greeting, the unnamed name and the empty chair only make sense
together.

The output is fully deterministic: a fixed string, written verbatim.
Exact size: 179 characters / 179 bytes total (To: line 38 chars,
message line 139 chars, well under the 260 total / 200 message caps),
so the gate passes with room to spare.
"""

import os

ENTRY = (
    "To: the night guard at my old building\n"
    "You said good morning for six years and I never learned your name, "
    "and the morning your chair was empty was the first time I wanted to ask.\n"
)


def main() -> None:
    text = ENTRY
    # Gate: 1-260 characters total, UTF-8, message line at most 200 chars.
    assert 1 <= len(text) <= 260, f"entry length {len(text)} out of range"
    lines = text.rstrip("\n").split("\n")
    assert len(lines) == 2, f"expected exactly 2 lines, got {len(lines)}"
    assert lines[0].startswith("To: "), "first line must be a To: line"
    assert len(lines[1]) <= 200, f"message line {len(lines[1])} chars > 200"
    assert text.strip(), "entry must not be only whitespace"
    text.encode("utf-8")

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


if __name__ == "__main__":
    main()
