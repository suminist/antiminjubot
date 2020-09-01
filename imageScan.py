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
import math

np.set_printoptions(threshold=sys.maxsize)

x1 = 450
x2 = 510
y1 = 934
y2 = 949

def snipecode():
    startTime = time.time()

    im = PIL.ImageGrab.grab(bbox=(x1, y1, x2, y2))

    # im.show()

    immatrix = np.array(im)
    immatrixT = immatrix.T[0]

    thresholdIndices0 = immatrixT < 160 #160
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

    # print(score)
    # print(zero)
    # print(nonzero)
    # print(changes)
    # print(length)

    code = ""
    
    if length == 9:
        immatrixTsplit = immatrixTsplit[1:8]

    length = np.shape(immatrixTsplit)[0]

    if length != 7:
        print("Error Code L" + str(length) +
              ": Error occurred while extracting letters from image. Please contact Rasmit#2547 with a screenshot of the logs.")
        # im.show()
        return

    # temp_prefix = "B9O2"
    # os.mkdir('./tests/' + temp_prefix)

    for i in range(4):
        code += read(immatrixTsplit[2 * i], i)

        # img = Image.fromarray(immatrixTsplit[2 * i]).save('./tests/' + temp_prefix + '/' + str(i) + '.png')
        # np.save('./tests/' + temp_prefix + '/' + str(i), immatrixTsplit[2 * i])

        # img = Image.fromarray(immatrixTsplit[2 * i]).save('./tests/' + temp_prefix + '/' + temp_prefix[i] + '.png')
        # np.save('./tests/' + temp_prefix + '/' + temp_prefix[i], immatrixTsplit[2 * i])

    print(code)

    if ("I" in code or "1" in code):
        print("This ain't it chief")
        # im.show()
    else:
        pyautogui.click(900, 950)
        pyautogui.typewrite('!claim ' + code)
        pyautogui.hotkey('enter')

        # temp_prefix = str(startTime)[-6:]
        # os.mkdir('./tests/' + temp_prefix)

        # for i in range(4):
        #     img = Image.fromarray(immatrixTsplit[2 * i]).save('./tests/' + temp_prefix + '/' + str(i) + '.png')
        #     np.save('./tests/' + temp_prefix + '/' + str(i), immatrixTsplit[2 * i])

    endTime = time.time()
    print("Start time: " + str(startTime))
    print("End Time: " + str(endTime))

    print("Elapsed Time: " + str(endTime - startTime) + " seconds")

def read(matrix, index):
    if (index == 0 or index == 2):
        characters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q",
                  "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
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
                    l = size0[0] - size1[0]
                    m = size0[1] - size1[1]

                    a = math.ceil(l/2)
                    b = math.ceil(m/2)
                    
                    pad_size0 = ((0,0), (0,0))
                    pad_size1 = ((a, l - a), (b, m - b))  # size0 extrema
                else:  # make size10 bigger, make size01 bigger
                    l = size1[1] - size0[1]
                    m = size0[0] - size1[0]

                    a = math.ceil(l/2)
                    b = math.ceil(m/2)
                    
                    pad_size0 = ((0,0), (a, l - a))
                    pad_size1 = ((b, m - b), (0,0))
            else:
                if (size0[1] > size1[1]):  # make size00 bigger, make size11 bigger
                    l = size1[0] - size0[0]
                    m = size0[1] - size1[1]

                    a = math.ceil(l/2)
                    b = math.ceil(m/2)
                    
                    pad_size0 = ((a, l - a), (0, 0))
                    pad_size1 = ((0, 0), (b, m - b))
                else:  # make size00 bigger, make size01 bigger
                    l = size1[0] - size0[0]
                    m = size1[1] - size0[1]

                    a = math.ceil(l/2)
                    b = math.ceil(m/2)
                    
                    # size1 extrema
                    pad_size0 = ((a, l - a), (b, m - b))
                    pad_size1 = ((0, 0), (0, 0))

            # print(pad_size0)
            # print(pad_size1)

            matrix = np.pad(matrix, pad_width=pad_size0, mode='constant', constant_values=0)
            sampleQ = np.pad(sampleQ, pad_width=pad_size1, mode='constant', constant_values=0)

            img0 = Image.fromarray(matrix).save('./tests/testing/' + character + str(index) + '.png')
            img1 = Image.fromarray(sampleQ).save('./tests/testing/' + character + str(index) + 'control.png')

            size0 = np.shape(matrix)
            size1 = np.shape(sampleQ)

            # print(size0)
            # print(size1)

        difference = np.subtract(sampleQ, matrix)
        score = np.sum(difference)
        scores.append(score)

    result = characters[scores.index(min(scores))]

    print(scores)
    print(result)

    return result

def main():
    snipelist = ['01', '09', '16', '24', '31', '39', '46', '54']

    while True:
        t = time.localtime()
        current_time = time.strftime("%H:%M:%S", t)
        current_time = current_time.split(':')

        if current_time[1] in snipelist:
            snipecode()
        else:
            print(f'cycling: {current_time[0]}:{current_time[1]} - IZ*ONECord')
            time.sleep(5)
            main()

def loop():
    while True:
        time.sleep(2)
        snipecode()

def convert():
    characters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q",
        "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

    for character in characters:
        arr = np.load('./characters/' + character + '.npy')
        img = Image.fromarray(arr.T)
        img.save('./charactersPNG/' + character + '.png')


snipecode()
# main()
# loop()
# convert()
