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

x1 = 450
x2 = 510
y1 = 934
y2 = 949

def snipecode():
    im = PIL.ImageGrab.grab(bbox=(x1, y1, x2, y2))

    # im.show()

    immatrix = np.array(im)
    immatrixT = immatrix.T[0]

    print(np.shape(immatrix))
    print(np.shape(immatrixT))

    thresholdIndices0 = immatrixT < 160
    immatrixT[thresholdIndices0] = 0

    thresholdIndices1 = immatrixT > 200
    immatrixT[thresholdIndices1] = 255

    # img = Image.fromarray(immatrixT.T).show()

    score = np.sum(immatrixT, axis=1)

    thresholdIndices2 = score != 0
    score[thresholdIndices2] = 1

    zero = np.where(score == 0)
    nonzero = np.where(score != 0)
    changes = np.where(np.diff(score))[0]+1
    immatrixTsplit = np.split(immatrixT, changes)

    print(score)
    print(zero)
    print(nonzero)
    print(changes)
    print(np.shape(immatrixTsplit))

    file2write = open("matrix", 'w')
    file2write.write(str(immatrixT))
    file2write.close()

    file2write = open("matrix1", 'w')

    for i in range(9):
        file2write.write(str(i) + "\n" + str(immatrixTsplit[i]) + "\n")

    file2write.close()

def main():
    snipecode()

main()
