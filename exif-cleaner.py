from PIL import Image
import sys

# Scrubs exif metadata from images

if len(sys.argv) <= 1:
    print "the image file is a required argument"
    sys.exit(1)

fn_in = sys.argv[1]
print "reading", fn_in

im = Image.open(fn_in)
print "image opened"

data = list(im.getdata())
image_without_exif = Image.new(im.mode, im.size)
image_without_exif.putdata(data)
print "exif information removed"

fn_out = ".".join(fn_in.split('.')[0:-1]) + '_no_exif.' + fn_in.split('.')[-1]
image_without_exif.save(fn_out)
print "saved to", fn_out
