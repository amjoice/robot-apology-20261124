#!/usr/bin/env python3
"""The Robot Apology — make.fun entry.

Writes a two-line robot confession to /output/entry.txt.

Line one owns one specific mistake: the robot sent two messages to
the wrong people, each message reaching exactly the person it was
never meant for. Line two names the lesson that mistake teaches and
the changed behaviour that follows from it: match the name on the
screen to the message in hand before pressing send.

Stdlib only. Deterministic: the same text on every run, no network,
no input files, no randomness.
"""

import os

LINE_ONE = (
    "I'm sorry I texted your dentist the grocery list "
    "and your grocer the appointment time."
)
LINE_TWO = (
    "I now match the name on the screen to the message in my hand "
    "before I press send."
)

ENTRY = LINE_ONE + "\n" + LINE_TWO


def build_entry() -> str:
    """Assemble the two-line confession and check it against the gate."""
    text = ENTRY
    if not text.strip():
        raise SystemExit("entry must not be only white space")
    if not 1 <= len(text) <= 400:
        raise SystemExit("entry must be 1-400 characters, got %d" % len(text))
    lines = text.split("\n")
    if len(lines) != 2:
        raise SystemExit("entry must be exactly two lines, got %d" % len(lines))
    for line in lines:
        if line != line.strip() or not line.endswith((".", "!", "?")):
            raise SystemExit("each line must be one clean sentence: %r" % line)
    return text


def main() -> None:
    text = build_entry()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
