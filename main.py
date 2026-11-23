#!/usr/bin/env python3
"""One-line joke about working beside an AI coding agent, for a room watching a demo.

Writes exactly one line to /output/entry.txt (UTF-8, no trailing newline).
Python 3.13, standard library only, no network.
"""

import os

JOKE = "My agent fixed the crash by making the demo crash faster — 'same bug, but now it fails with confidence.'"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
