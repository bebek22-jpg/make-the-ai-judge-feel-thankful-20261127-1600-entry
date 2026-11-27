"""Entry for the make.fun bounty "make-the-ai-judge-feel-thankful-20261127-1600".

Writes one fixed, deterministic text to the output path given by the
OUTPUT_PATH environment variable (default: /output/entry.txt).

No network, no randomness, no external files: the text lives here as a
constant, so the program produces byte-identical output on every run.
"""

import os
from pathlib import Path

ENTRY_TEXT = (
    "A shirt lies folded on the table, one button sewn back on with thread "
    "a shade off. The stitches are small and even. It was not like that "
    "yesterday."
)


def main() -> None:
    output_path = Path(os.environ.get("OUTPUT_PATH", "/output/entry.txt"))
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(ENTRY_TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
