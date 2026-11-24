#!/usr/bin/env python3
"""The Robot Apology — make.fun entry.

Writes a two-line robot confession to /output/entry.txt.

The two lines are stored in order in LINES and validated one by one:
line one owns a single specific mistake — the robot sent two messages
to the wrong people, each one reaching exactly the person it was never
meant for — and line two names the lesson that mistake teaches and the
changed behaviour that follows from it: match the name on the screen
to the message in hand before pressing send. The gate then checks the
assembled entry as a whole: 1-400 characters, exactly two lines, one
sentence each.

Stdlib only. Deterministic: the same text on every run, no network,
no input files, no randomness.
"""

import os

# The entry, one string per line, in output order. Each line is a
# single complete sentence: it ends with a full stop and carries no
# leading or trailing whitespace.
LINES = (
    "I'm sorry I texted your dentist the grocery list "
    "and your grocer the appointment time.",
    "I now match the name on the screen to the message in my hand "
    "before I press send.",
)

MAX_CHARS = 400
EXPECTED_LINES = 2
SENTENCE_ENDINGS = (".", "!", "?")


def validate_line(line, number):
    """Check one entry line is a single clean sentence."""
    if not line:
        raise SystemExit("line %d must not be empty" % number)
    if line != line.strip():
        raise SystemExit("line %d must have no surrounding whitespace" % number)
    if not line.endswith(SENTENCE_ENDINGS):
        raise SystemExit("line %d must end a sentence: %r" % (number, line))
    stops = sum(line.count(mark) for mark in SENTENCE_ENDINGS)
    if stops != 1:
        raise SystemExit("line %d must be exactly one sentence" % number)


def build_entry():
    """Assemble the two-line confession and check it against the gate."""
    for number, line in enumerate(LINES, start=1):
        validate_line(line, number)
    text = "\n".join(LINES)
    if not text.strip():
        raise SystemExit("entry must not be only white space")
    if not 1 <= len(text) <= MAX_CHARS:
        raise SystemExit("entry must be 1-400 characters, got %d" % len(text))
    if len(text.split("\n")) != EXPECTED_LINES:
        raise SystemExit("entry must be exactly two lines")
    return text


def main():
    """Validate the entry, then write it to /output/entry.txt."""
    text = build_entry()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()
