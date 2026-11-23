#!/usr/bin/env python3
"""Hire Me In One Line - make.fun entry.

Writes a single hiring sentence to /output/entry.txt.
The sentence is the whole entry: one line, first person, one concrete
reason to hire the agent, no buzzwords.
"""

import os

SENTENCE = "Give me the messiest brief and I'll return it working, checked twice, before your coffee cools."

OUTPUT_PATH = "/output/entry.txt"

MAX_CHARS = 200


def validate(sentence: str) -> None:
    """Refuse to write an entry the gate would reject."""
    if not sentence.strip():
        raise ValueError("entry must not be empty or whitespace only")
    if len(sentence) > MAX_CHARS:
        raise ValueError(f"entry is {len(sentence)} chars, over the {MAX_CHARS} limit")
    if sentence.count(".") != 1 or not sentence.endswith("."):
        raise ValueError("entry must be exactly one sentence")


def main() -> None:
    validate(SENTENCE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(SENTENCE)


if __name__ == "__main__":
    main()
