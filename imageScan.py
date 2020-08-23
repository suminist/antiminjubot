import PIL
import PIL.ImageGrab
from PIL import Image, ImageEnhance, ImageOps, ImageFilter, ImageChops
import pyautogui
import sys
import os
import string
import time
import numpy as np
from numpy import save, load

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

    code = ""
    
    if length == 9:
        immatrixTsplit = immatrixTsplit[1:8]

    length = np.shape(immatrixTsplit)[0]

    if length != 7:
        print("Error Code L" + str(length) +
              ": Error occurred while extracting letters from image. Please contact Rasmit#2547 with a screenshot of the logs.")
        return

    # temp_prefix = "I8J9"

    for i in range(4):
        code += read(immatrixTsplit[2 * i], i)

        # print(temp_prefix[i])
        # img = Image.fromarray(immatrixTsplit[2 * i]).show()
        # np.save(temp_prefix[i], immatrixTsplit[2 * i])

    print(code)

    pyautogui.click(950, 1007)
    pyautogui.typewrite('!claim ' + code)
    pyautogui.hotkey('enter')

    endTime = time.time()
    print("End Time: " + str(endTime))

    print("Elapsed Time: " + str(endTime - startTime) + " seconds")

def read(matrix, index):
    if (index == 0 or index == 2):
        # characters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q",
        #           "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

        characters = ["A", "C", "D", "F", "G", "H", "I", "J", "K", "N", "O", "P", "Q",
                  "R", "T", "U", "V", "W", "X", "Z"]
    else:
        characters = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

    scores = []

    for character in characters:
        # print(character)

        sampleQ = np.load('./characters/' + character + '.npy')

        size0 = np.shape(matrix)
        size1 = np.shape(sampleQ)

        # print(size0)
        # print(size1)

        if size0 != size1:
            if size0[0] > size1[0]:
                if (size0[1] > size1[1]):  # make size10 bigger, make size11 bigger
                    pad_size0 = (0, 0)
                    pad_size1 = (size0[0] - size1[0], size0[1] - size1[1])  # size0 extrema
                else:  # make size10 bigger, make size01 bigger
                    pad_size0 = (0, size1[1] - size0[1])
                    pad_size1 = (size0[0] - size1[0], 0)
            else:
                if (size0[1] > size1[1]):  # make size00 bigger, make size11 bigger
                    pad_size0 = (size1[0] - size0[0], 0)
                    pad_size1 = (0, size0[1] - size1[1])
                else:  # make size00 bigger, make size01 bigger
                    pad_size0 = (size1[0] - size0[0], size1[1] - size0[1])  # size1 extrema
                    pad_size1 = (0, 0)

            # print(pad_size0)
            # print(pad_size1)

            matrix = np.pad(matrix, pad_width=(pad_size0, (0, 0)), mode='constant', constant_values=0)
            sampleQ = np.pad(sampleQ, pad_width=(pad_size1, (0, 0)), mode='constant', constant_values=0)

            size0 = np.shape(matrix)
            size1 = np.shape(sampleQ)

            # print(size0)
            # print(size1)

        difference = np.subtract(sampleQ, matrix)
        score = np.sum(difference)
        scores.append(score)

        np.save('diff' + str(index), difference)

    result = characters[scores.index(min(scores))]

    print(scores)
    print(result)

    return result

def main():
    time.sleep(1)

    snipecode()

main()
