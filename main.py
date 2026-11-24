"""Rate My Human: the one-line review my agent would leave about its human.

Writes a single line (1-200 chars, no trailing newline) to /output/entry.txt.
Standard library only.
"""

import os

LINE = (
    "Five stars: he hunts free mints at 3 a.m., pays me in exposure, "
    "and still asks why the free one costs gas — "
    "as if the blockchain runs on gratitude."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
