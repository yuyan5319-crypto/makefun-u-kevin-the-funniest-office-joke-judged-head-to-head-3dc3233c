#!/usr/bin/env python3
"""The Funniest Office Joke, Judged Head to Head.

One short line about office life is the whole entry. This program writes
that single line to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt
when run outside the grader).

The joke, written for this bounty:

    I asked the printer for a raise; it jammed, which is still more
    feedback than my manager ever gave me.

Why this line: the setup is an absurd but instantly recognisable office
moment (asking the printer, the one machine everyone begs, for a raise);
the turn is the jam -- the printer's only reply -- and the punchline lands
last, reframing the jam as more feedback than a manager ever gives.
Every word earns its place, and the line is one sentence, well under the
200-character gate.
"""

import os
import sys

JOKE = "I asked the printer for a raise; it jammed, which is still more feedback than my manager ever gave me."

MAX_CHARS = 200


def validate(text: str) -> None:
    """Mirror the sealed gate scorer: 1-200 chars, not only whitespace."""
    if not (1 <= len(text) <= MAX_CHARS):
        raise SystemExit(f"entry is {len(text)} chars, gate needs 1-{MAX_CHARS}")
    if not text.strip():
        raise SystemExit("entry is only whitespace")
    text.encode("utf-8")  # raises if not valid UTF-8


def main() -> int:
    validate(JOKE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE)
    print(f"wrote {len(JOKE)} chars to {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
