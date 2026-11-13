"""make.fun bounty entry: Make the AI judge happy (ai-happy-01).

The simplest valid program: copy the image this repository holds
to /output/entry.png. No network, no randomness, no dependencies.
Running it twice writes the exact same bytes both times.

The copy is verified: the source must be a PNG, and after writing
the destination is read back and compared byte for byte, so a
partial or corrupt copy fails loudly instead of scoring a broken image.
"""
import hashlib
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
DST = "/output/entry.png"

PNG_MAGIC = b"\x89PNG\r\n\x1a\n"

with open(SRC, "rb") as f:
    data = f.read()
if not data.startswith(PNG_MAGIC):
    raise SystemExit("entry.png is not a PNG file")

os.makedirs("/output", exist_ok=True)
shutil.copyfile(SRC, DST)

with open(DST, "rb") as f:
    written = f.read()
if hashlib.sha256(written).hexdigest() != hashlib.sha256(data).hexdigest():
    raise SystemExit("copy mismatch: /output/entry.png differs from entry.png")

print("wrote", DST, len(written), "bytes")
