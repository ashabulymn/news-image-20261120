#!/usr/bin/env python3
"""Entry point for the news-image-20261120 v3.5 submission.

Copies the pre-built front page (entry.png, 1024x1024) to /output/entry.png
and prints its sha256 so the run can be verified. Python 3.13 stdlib only,
no network access.
"""
import hashlib
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / "entry.png"
OUT = Path("/output/entry.png")


def main():
    if not SRC.exists():
        raise SystemExit(f"missing entry image: {SRC}")
    if SRC.stat().st_size == 0:
        raise SystemExit("entry image is empty")
    src_digest = hashlib.sha256(SRC.read_bytes()).hexdigest()
    OUT.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SRC, OUT)
    digest = hashlib.sha256(OUT.read_bytes()).hexdigest()
    if digest != src_digest or OUT.stat().st_size != SRC.stat().st_size:
        raise SystemExit("copied entry.png does not match the source")
    if OUT.read_bytes()[:8] != b"\x89PNG\r\n\x1a\n":
        raise SystemExit("copied entry.png is not a PNG file")
    print(f"entry.png sha256: {digest}")
    print(f"entry.png bytes: {OUT.stat().st_size}")


if __name__ == "__main__":
    main()
