from __future__ import print_function
from wand.image import Image
import glob

width=612
height=612

for filename in glob.glob('*.jpg'):
        with Image(filename=filename) as original:
            original.transform(resize="%dx%d>" % (width, height))
#            outerImg.format = original.format.lower()
#            outerImg.composite(original, left=int((width - original.width)/2), top=int((height-original.height)/2))
#            original.resize(height=612, width=612)
            original.save(filename='new_'+filename)