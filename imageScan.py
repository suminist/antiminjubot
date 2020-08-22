import PIL
import PIL.ImageGrab
from PIL import Image, ImageEnhance, ImageOps, ImageFilter, ImageChops
import os
import string
import datetime
import time
import numpy as np
import sys

np.set_printoptions(threshold=sys.maxsize)

x1 = 454
x2 = 506
y1 = 934
y2 = 949

def snipecode():
    code = "Z8F0"

    # for a in range(4):
    #     addX = a * 13
        # im = PIL.ImageGrab.grab(bbox=(x1 + addX, y1, x1 + addX + 13, y2))  # X1,Y1,X2,Y2 # A
    im = PIL.ImageGrab.grab(bbox=(x1, y1, x2, y2))  # X1,Y1,X2,Y2 # B
    immatrix = np.array(im).T

    im.show()
    print(np.shape(immatrix))

    # file2write = open("matrix" + str(a), 'w') # A
    file2write = open("matrix", 'w') # B
    file2write.write(str(immatrix))
    file2write.close()

    # if a == 0:
    #     mse(immatrix, immatrix)


def snipecode1():
    code = "Z8F0"

    addX1 = 1 * 13
    addX2 = 3 * 13

    im1 = PIL.ImageGrab.grab(bbox=(x1 + addX1, y1, x1 + addX1 + 13, y2))  # X1,Y1,X2,Y2
    immatrix1 = np.array(im1)

    im2 = PIL.ImageGrab.grab(bbox=(x1 + addX2, y1, x1 + addX2 + 13, y2))  # X1,Y1,X2,Y2
    immatrix2 = np.array(im2)

    mse(immatrix1, immatrix2)

    im1.show()
    im2.show()

def mse(imageA, imageB):
	error = np.sum((imageA - imageB.astype("float")) ** 2)
	error /= float(imageA.shape[0] * imageA.shape[1])

	print(error)

def main():
    snipecode()
    # snipecode1()

main()
