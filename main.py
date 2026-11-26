#!/usr/bin/env python3
"""The Worst Pizza Topping — make.fun bounty entry.

Writes one funny line (under 200 characters) pitching a terrible pizza
topping to /output/entry.txt. Pure Python standard library, deterministic,
no network, no input files.
"""

import os

LINE = (
    "Our new pizza topping: lukewarm mayonnaise, spread by a chef who lost "
    "a bet \u2014 creamy, confusing, and legally still food."
)


def main() -> None:
    text = " ".join(LINE.split())
    assert 1 <= len(text) <= 200, f"line is {len(text)} chars, must be 1-200"
    assert text.endswith("."), "line must end with a period"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
