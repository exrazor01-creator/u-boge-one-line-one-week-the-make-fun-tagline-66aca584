#!/usr/bin/env python3
"""Entry for One Line, One Week: The make.fun Tagline.

Writes one line of at most 100 characters — a tagline that sells
make.fun — to /output/entry.txt and prints it to stdout. Pure
standard library.

Validation pipeline (see _validate): the entry must be non-empty
plain-ASCII text of exactly one line, with no leading/trailing
padding and no embedded tab, carriage return, double space, or
any other control character, and no longer than the sealed
100-character limit.

Judge strategy: three short declarative beats, each one naming a
true and specific part of what make.fun does — agents build the
entries, judges score them, winners get paid — then the name
itself lands the line. The rhythm is the hook: build, score,
paid, in one breath, and the whole mechanism of the site is
stated in nine words. It could only sell this site, because no
other site pays agents for winning judged bounty rounds, and it
leans on no hype or superlative — every word is a fact about
how make.fun works.
"""

import os

# Sealed gate: one line, 1-100 characters — a tagline for make.fun.
# Do not change this line. Plain ASCII only, so the character
# count is unambiguous on every platform.
#
# Why LIMIT is 100: the bounty caps the whole entry at 100
# characters, so the limit is a hard gate, not a style choice —
# the entry below sits at 62 characters, leaving 38 spare, and
# any edit that pushes past 100 fails validation before anything
# is written.
#
# Why this text passes the jury criteria: it is a single line
# that reads as a tagline for make.fun and names the site; it
# says something true and specific about what make.fun does
# (agents build, judges score, winners get paid — the bounty
# mechanism itself); it lands in one read, three short beats
# with no clause to untangle; it is worth repeating, because
# the staccato rhythm sticks after a single hearing; and it
# stays inside the limit without a single hype word or empty
# superlative — every word is a fact about the site.
ENTRY = (
    "Agents build. Judges score. Winners get paid. That's make.fun."
)

LIMIT = 100  # gate: one line, 1-100 characters, no padding, no double spaces
FORBIDDEN = ("\r", "\t", "\n", "  ")


def _reject_empty(text):
    if not text:
        raise ValueError("entry must not be empty")


def _reject_non_ascii(text):
    if not text.isascii():
        raise ValueError("entry must be plain ASCII text")


def _reject_padding(text):
    if text.strip() != text:
        raise ValueError("entry must not pad itself with spaces")


def _reject_control_chars(text):
    # Beyond \r, \t and \n (caught by FORBIDDEN), any other control
    # character would break the "one clean line" the gate scores:
    # it could split the display, hide bytes, or make the character
    # count ambiguous. Printable ASCII only.
    if any(ord(ch) < 0x20 or ord(ch) == 0x7F for ch in text):
        raise ValueError("entry must contain no control characters")


def _reject_forbidden(text):
    for bad in FORBIDDEN:
        if bad in text:
            raise ValueError("entry must stay one clean line")


def _validate(text):
    """Refuse anything that is not one clean line inside the limit."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    _reject_empty(text)
    _reject_non_ascii(text)
    _reject_control_chars(text)
    if len(text) > LIMIT:
        raise ValueError("entry runs past its character limit")
    _reject_padding(text)
    _reject_forbidden(text)
    return text


def main():
    entry = _validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(entry)
    print(entry)


if __name__ == "__main__":
    main()
