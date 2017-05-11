import gevent.monkey
import time

from PIL import Image, ImageDraw, ImageFont

gevent.monkey.patch_all()

def create_image(id):
	file_name = "hasil/%s.png" % id
	img = Image.new("RGB", (512, 512), "black")
	draw = ImageDraw.Draw(img)
	font = ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeSans.ttf", 200)
	draw.text((10, 25), str(id), font=font)
	img.save(file_name, "PNG") 

def runme(id):
    print "Starting ID %s" % id
    create_image(id)
    print "ID %s Done" % id

jobs = [gevent.spawn(runme, _id) for _id in range(1000)]

gevent.wait(jobs)
