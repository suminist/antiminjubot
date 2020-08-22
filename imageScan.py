import PIL
import PIL.ImageGrab
from PIL import Image, ImageEnhance, ImageOps, ImageFilter, ImageChops
import sys
import os
import string
import time
import numpy as np
from skimage.io import imread, imsave

np.set_printoptions(threshold=sys.maxsize)

x1 = 450
x2 = 510
y1 = 934
y2 = 949

def snipecode():
    startTime = time.time()
    print("Start time: " + str(startTime))

    im = PIL.ImageGrab.grab(bbox=(x1, y1, x2, y2))

    # im.show()

    immatrix = np.array(im)
    immatrixT = immatrix.T[0]

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
    length = np.shape(immatrixTsplit)[0]

    print(score)
    print(zero)
    print(nonzero)
    print(changes)
    print(length)

    file0 = open("matrix2", 'w')

    code = ""
    
    if length == 9:
        immatrixTsplit = immatrixTsplit[1:8]

    length = np.shape(immatrixTsplit)[0]

    if length != 7:
        print("Error Code L" + str(length) +
              ": Error occurred while extracting letters from image. Please contact Rasmit#2547 with a screenshot of the logs.")
        return

    for i in range(4):
        code += read(immatrixTsplit[2 * i])

        fileN = open("v" + str(i), "w")
        fileN.write(str(immatrixTsplit[2 * i]))
        fileN.close()

        file0.write(str(i) + "\n" + str(immatrixTsplit[2 * i]) + "\n")

    file0.close()

    # file1 = open("matrix", 'w')
    # file1.write(str(immatrixT))
    # file1.close()

    endTime = time.time()
    print("End Time: " + str(endTime))

    print("Elapsed Time: " + str(endTime - startTime) + " seconds")

def read(matrix):
    return "A"

def main():
    snipecode()
    # testLetter("Q")

main()
