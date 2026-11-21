#!/usr/bin/env python3
"""Entry for make.fun news-image-20261120 (v3.3).

v3.3 is a 300px-legibility revision of v3.2: same 34 verified stories,
bigger hero banners and headlines, larger KPI numbers and card titles,
so the front page still reads at about 300 pixels across.

Copies the pre-built front page (entry.png, rendered in-session from
page-v3.3.html) to /output/entry.png. Stdlib only, no network, deterministic.
"""
import hashlib
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / "entry.png"
DST = Path("/output/entry.png")


def main() -> None:
    DST.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SRC, DST)
    print("entry.png sha256:", hashlib.sha256(DST.read_bytes()).hexdigest())


if __name__ == "__main__":
    main()
