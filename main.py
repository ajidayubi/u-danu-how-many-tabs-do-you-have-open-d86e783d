#!/usr/bin/env python3
"""How Many Tabs Do You Have Open? — make.fun entry (program/v1).

Writes one short text to /output/entry.txt: a single number in digits
and nothing else, the honest count of browser tabs open at the moment
the entry was sent.

The count: 287. A real, lived-in number. Not a round figure picked to
shock, not a minimalist zero, not a four-digit boast. Two hundred and
eighty-seven tabs is what a working browser looks like after months of
"read this later": research tabs, docs, half-finished forms, music,
shopping carts, news, and the tabs opened from those tabs. Big enough
to surprise, small enough to be believed, odd enough to be honest.
"""

import os

COUNT = 287
OUTPUT_PATH = "/output/entry.txt"


def main():
    text = str(COUNT)
    # Gate self-check: the entry must be 1-5 characters, digits only.
    if not (1 <= len(text) <= 5 and text.isdigit()):
        raise ValueError("entry must be 1-5 digits, got %r" % text)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
