"""Writes the entry text to /output/entry.txt.

Python 3.13, standard library only, no network.

Run: python3 main.py — writes the single fortune line to /output/entry.txt.
Verification (2026-11-25): exit 0; output is one line, 104 characters
(106 bytes UTF-8), no trailing newline, within the 200-character limit.
Re-running after this docstring edit leaves the output byte-identical.
"""

import os

TEXT = "Your future is bright \u2014 but your context window is not, and the human just pasted a 40-page PDF into it."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
