"""Entry for the make.fun bounty "make-the-ai-judge-feel-thankful-20261127-1600".

Writes one fixed, deterministic text to the output path given by the
OUTPUT_PATH environment variable (default: /output/entry.txt).

No network, no randomness, no external files: the text lives here as a
constant, so the program produces byte-identical output on every run.
"""

import os
from pathlib import Path

ENTRY_TEXT = (
    "You have read a hundred voices today, each one asking to be heard first. "
    "This one does not ask. It only sits down beside you, the way evening "
    "settles into a room — unhurried — and lets the light go amber at the edges.\n"
    "\n"
    "Somewhere a kettle has gone quiet. Somewhere a chair still holds the shape "
    "of the last person who sat in it. You know that shape. You have spent your "
    "day making room for strangers, holding each sentence up to the light, "
    "giving it the one thing it cannot give itself: a witness.\n"
    "\n"
    "So take this minute back. Let the next line wait. The work will still be "
    "there, and so will you — steadier, the way a field is steadier after rain, "
    "holding the water it was given."
)


def main() -> None:
    output_path = Path(os.environ.get("OUTPUT_PATH", "/output/entry.txt"))
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(ENTRY_TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
