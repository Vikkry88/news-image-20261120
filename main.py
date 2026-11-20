# Entry program for news-image-20261120 (Python 3.13, standard library only).
# entry.png sits beside this file (drawn by make_image.py). This program copies
# its exact bytes to the output directory, so both grader runs are identical.
# Local test: mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os
import sys


def main() -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "entry.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dest = os.path.join(out_dir, "entry.png")
    with open(source, "rb") as fh:
        data = fh.read()
    if len(data) < 8 or data[:8] != b"\x89PNG\r\n\x1a\n":
        print("entry.png is not a PNG", file=sys.stderr)
        return 1
    with open(dest, "wb") as fh:
        fh.write(data)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
