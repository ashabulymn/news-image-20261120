#!/usr/bin/env python3
"""Write the 20 November 2026 world-news front page to /output/entry.png.

v1.7: a premium one-page newspaper rebuilt in-session from a reference
layout (globe masthead, three photo heroes, twelve Global Developments
cards with date checks, world map with a numbered index). 23 stories,
every one first reported on Friday 20 November 2026.

The picture itself is pre-built (1024x1024, under 1 MiB) and stored in
this repository as entry.png. This program only copies it, with no
network and no randomness, so running it twice writes identical bytes.
"""
import hashlib
import os
import pathlib
import shutil
import sys

HERE = pathlib.Path(__file__).resolve().parent
SOURCE = HERE / "entry.png"
# The grader sets /output; a local run can point elsewhere instead.
OUTDIR = pathlib.Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
TARGET = OUTDIR / "entry.png"


def main() -> int:
    if not SOURCE.is_file():
        print(f"entry image missing: {SOURCE}", file=sys.stderr)
        return 1
    OUTDIR.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SOURCE, TARGET)
    print(f"wrote {TARGET} sha256={hashlib.sha256(TARGET.read_bytes()).hexdigest()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
