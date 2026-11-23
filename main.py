#!/usr/bin/env python3
"""One-line joke about working beside an AI coding agent, for a room watching a demo.

Writes exactly one line to /output/entry.txt (UTF-8, no trailing newline).
Python 3.13, standard library only, no network.
"""

import os

JOKE = "My agent fixed the crash by making the demo crash faster — 'same bug, but now it fails with confidence.'"


def build_joke() -> str:
    """Produce the one-line joke for the demo."""
    return JOKE


def validate_joke(text: str) -> None:
    """Require a single line of 1-280 Unicode code points."""
    if not 1 <= len(text) <= 280:
        raise SystemExit(f"invalid joke: expected 1-280 characters, got {len(text)}")
    if "\n" in text or "\r" in text:
        raise SystemExit("invalid joke: must be a single line")


def main() -> None:
    joke = build_joke()
    validate_joke(joke)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(joke)


if __name__ == "__main__":
    main()
