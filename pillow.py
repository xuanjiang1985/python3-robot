# !/usr/bin/python3

import os, sys
from PIL import Image

# im = Image.open("exam.png")
# print(im.format, im.size, im.mode)

for infile in sys.argv[1:]:
    f, e = os.path.splitext(infile)
    outfile = f + ".jpg"
    if infile != outfile:
        try:
            Image.open(infile).save(outfile)
        except IOError:
            print("cannot convert", infile)