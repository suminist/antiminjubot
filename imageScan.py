import PIL
from PIL import Image, ImageEnhance, ImageOps, ImageFilter, ImageChops
import PIL.ImageGrab

x1 = 454
y1 = 934
y2 = 950

def tti():
    for a in range(4):
        addX = a * 13
        im = PIL.ImageGrab.grab(bbox=(x1 + addX, y1, x1 + addX + 13, y2))  # X1,Y1,X2,Y2
        im.show()

def timecheck():
    tti()

timecheck()
