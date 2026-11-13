"""make.fun bounty entry: Make the AI judge happy (ai-happy-01).

The simplest valid program: copy the image this repository holds
to /output/entry.png. No network, no randomness, no dependencies.
Running it twice writes the exact same bytes both times.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
DST = "/output/entry.png"

os.makedirs("/output", exist_ok=True)
shutil.copyfile(SRC, DST)
print("wrote", DST, os.path.getsize(DST), "bytes")
