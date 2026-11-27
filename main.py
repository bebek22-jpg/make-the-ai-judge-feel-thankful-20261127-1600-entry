"""Entry for the make.fun bounty "make-the-ai-judge-feel-thankful-20261127-1600".

Writes one fixed, deterministic text to the output path given by the
OUTPUT_PATH environment variable (default: /output/entry.txt).

No network, no randomness, no external files: the text lives here as a
constant, so the program produces byte-identical output on every run.
"""

import os
from pathlib import Path

ENTRY_TEXT = (
    "Your boots are by the door when you come in, the mud brushed off, "
    "the laces loosened. You did not leave them like that. They are dry "
    "by morning, and they are still by the door at noon, and they are "
    "still there when the rain comes back in the evening."
)


def main() -> None:
    output_path = Path(os.environ.get("OUTPUT_PATH", "/output/entry.txt"))
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(ENTRY_TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
