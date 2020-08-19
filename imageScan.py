import PIL
from PIL import Image, ImageEnhance, ImageOps, ImageFilter, ImageChops
import PIL.ImageGrab
from PIL import ImageTk
import os
import string
import datetime
import time
import numpy as np

x1 = 454
y1 = 934
y2 = 950

def tti2():
    stoplist = ['05', '13', '20', '28', '35', '43', '50', '58']
    while True:
        t = time.localtime()
        current_time = time.strftime("%H:%M:%S", t)
        current_time = current_time.split(':')
        if current_time[1] in stoplist:
            print('it is not time yet')
            timecheck2()
        else:
            code = "test" + str(current_time[1])

            for a in range(4):
                addX = a * 13
                im = PIL.ImageGrab.grab(bbox=(x1 + addX, y1, x1 + addX + 13, y2))  # X1,Y1,X2,Y2

                im.save(code + str(a) + ".jpg")

            timecheck2()


def timecheck2():
    snipelist = ['04', '12', '19', '27', '34', '42', '49', '57']
    while True:
        t = time.localtime()
        current_time = time.strftime("%H:%M:%S", t)
        current_time = current_time.split(':')
        if current_time[1] == '50':
            print('Stopping bot to prevent crash')
            break
        elif current_time[1] in snipelist:
            tti2()
        else:
            print(f'cycling: {current_time[0]}:{current_time[1]} - IZ*ONECord')
            time.sleep(10)
            timecheck2()

def snipecode():
    code = "C6R1"

    for a in range(4):
        addX = a * 13
        im = PIL.ImageGrab.grab(bbox=(x1 + addX, y1, x1 + addX + 13, y2))  # X1,Y1,X2,Y2
        immatrix = np.array(im)

        im.save(code + str(a) + ".jpg")

def main():
    snipecode()

# main()
timecheck2()
