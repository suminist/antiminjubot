import tkinter as tk
import pyautogui
import PIL
from PIL import Image, ImageEnhance, ImageOps, ImageFilter, ImageChops
import PIL.ImageGrab
import time
import datetime
import string
from pathlib import Path
import os
import sys
from PIL import ImageTk
import numpy as np
from numpy import save, load
import argparse

np.set_printoptions(threshold=sys.maxsize)

x1 = 450
x2 = 510
y1 = 934
y2 = 949

def tti2():
    stoplist = ['06', '14', '21', '29', '36', '44', '51', '59']
    
    while True:
        t = time.localtime()
        current_time = time.strftime("%H:%M:%S", t)
        current_time = current_time.split(':')

        if current_time[1] in stoplist:
            print('it is not time yet')
            timecheck2()
            return
        else:
            startTime = time.time()
            print("Start time: " + str(startTime))

            im = PIL.ImageGrab.grab(bbox=(x1, y1, x2, y2))

            immatrix = np.array(im)
            immatrixT = immatrix.T[0]

            thresholdIndices0 = immatrixT < 160
            immatrixT[thresholdIndices0] = 0

            thresholdIndices1 = immatrixT > 200
            immatrixT[thresholdIndices1] = 255

            score = np.sum(immatrixT, axis=1)

            thresholdIndices2 = score != 0
            score[thresholdIndices2] = 1

            zero = np.where(score == 0)
            nonzero = np.where(score != 0)
            changes = np.where(np.diff(score))[0]+1
            immatrixTsplit = np.split(immatrixT, changes)
            length = np.shape(immatrixTsplit)[0]

            code = ""
            
            if length == 9:
                immatrixTsplit = immatrixTsplit[1:8]
            elif length == 8:
                immatrixTsplit = immatrixTsplit[0:7]

            length = np.shape(immatrixTsplit)[0]

            if length != 7:
                print("Did not find code")

                return
            else:
                for i in range(4):
                    code += read(immatrixTsplit[2 * i], i)

                    img = Image.fromarray(immatrixTsplit[2 * i])
                    img.save('./codes/' + str(i) + '.png')

                print(code)

                if ("1" in code or "I" in code):
                    print("This ain't it, chief.")
                    return

                pyautogui.click(950, 1007)
                pyautogui.typewrite('!claim ' + code)
                pyautogui.hotkey('enter')

                endTime = time.time()
                print("End Time: " + str(endTime))

                print("Elapsed Time: " + str(endTime - startTime) + " seconds")

                return

        break


def read(matrix, index):
    if (index == 0 or index == 2):
        characters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q",
                      "R", "S", "T", "U", "V", "W", "X", "Z"]
    else:
        characters = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

    scores = []

    for character in characters:

        sampleQ = np.load('./characters/' + character + '.npy')

        size0 = np.shape(matrix)
        size1 = np.shape(sampleQ)

        if size0 != size1:
            if size0[0] > size1[0]:
                if (size0[1] > size1[1]):  # make size10 bigger, make size11 bigger
                    pad_size0 = (0, 0)
                    pad_size1 = (size0[0] - size1[0],
                                 size0[1] - size1[1])  # size0 extrema
                else:  # make size10 bigger, make size01 bigger
                    pad_size0 = (0, size1[1] - size0[1])
                    pad_size1 = (size0[0] - size1[0], 0)
            else:
                if (size0[1] > size1[1]):  # make size00 bigger, make size11 bigger
                    pad_size0 = (size1[0] - size0[0], 0)
                    pad_size1 = (0, size0[1] - size1[1])
                else:  # make size00 bigger, make size01 bigger
                    pad_size0 = (size1[0] - size0[0],
                                 size1[1] - size0[1])  # size1 extrema
                    pad_size1 = (0, 0)

            matrix = np.pad(matrix, pad_width=(pad_size0, (0, 0)),
                            mode='constant', constant_values=0)
            sampleQ = np.pad(sampleQ, pad_width=(
                pad_size1, (0, 0)), mode='constant', constant_values=0)

            size0 = np.shape(matrix)
            size1 = np.shape(sampleQ)

        difference = np.subtract(sampleQ, matrix)
        score = np.sum(difference)
        scores.append(score)

    result = characters[scores.index(min(scores))]

    print(scores)
    print(result)

    return result

def timecheck2():
    snipelist = ['05', '13', '20', '27', '35', '42', '50', '57']

    while True:
        t = time.localtime()
        current_time = time.strftime("%H:%M:%S", t)
        current_time = current_time.split(':')

        if current_time[1] in snipelist:
            tti2()
        else:
            print(f'cycling: {current_time[0]}:{current_time[1]} - IZ*ONECord')
            time.sleep(5)
            timecheck2()

parser = argparse.ArgumentParser()

parser.add_argument("-s", "--server", help="Server")

args = parser.parse_args()

if args.server == "izcord":
    timecheck2()

runGUI()

def runGUI():
    ht = 360
    wd = 600
    mvall = 0.5
    mvallh = 0.25
    root = tk.Tk()

    version = 'SYBot V.2.1.0-a.1'

    #main canvas
    canvas = tk.Canvas(root, height=ht, width=wd)
    canvas.pack()
    #background image
    background_img = ImageTk.PhotoImage(Image.open(r'32.png'))
    background_label = tk.Label(root, image=background_img)
    background_label.place(relx=0.5, rely=0.25, relwidth=mvall, relheight=0.5)
    #main frame
    #relx, rely in percentages
    frame = tk.Frame(root, bg='pink')
    frame.place(relx=0, rely=0, relwidth=1, relheight=0.25)

    label = tk.Label(frame, text='Starts bot instantly', bg='white')
    label.pack()

    button = tk.Button(frame, text="Start Bot", bg='#50A7AB',
                    fg='#000000', command=timecheck2)
    button.pack(side='bottom')

    #frame 2
    frame2 = tk.Frame(root, bg='#92F1FE')
    frame2.place(relx=0, rely=0.25, relwidth=mvall, relheight=mvallh)

    label2 = tk.Label(frame2, text="WeeeklyCord", bg='white')
    label2.pack()
    label2x = tk.Label(frame2, text="12 | 27 | 42 | 57", bg='white')
    label2x.pack()

    button2 = tk.Button(frame2, text="Start Bot", bg='#50A7AB',
                        fg='#000000', command=timecheck2)
    button2.pack(side='bottom')

    #frame 3
    frame3 = tk.Frame(root, bg='#F69AF8')
    frame3.place(relx=0, rely=0.5, relwidth=mvall, relheight=mvallh)

    label3 = tk.Label(frame3, text="IZ*ONECord", bg='white')
    label3.pack()
    label3x = tk.Label(
        frame3, text="04 | 12 | 19 | 27 | 34 | 42 | 49 | 57", bg="white")
    label3x.pack()

    button3 = tk.Button(frame3, text="Start Bot", bg='#50A7AB',
                        fg='#000000', command=timecheck2)
    button3.pack(side='bottom')

    #frame 4
    frame4 = tk.Frame(root, bg='#E2F89A')
    frame4.place(relx=0.25, rely=0.75, relwidth=mvall, relheight=mvallh)

    label4 = tk.Label(frame4, text="View scan area", bg='white')
    label4.pack()

    button4 = tk.Button(frame4, text="View area", bg='#50A7AB',
                        fg='#000000', command=timecheck2)
    button4.pack(side='bottom')

    #frame 5
    frame5 = tk.Frame(root, bg='#E2F89A')
    frame5.place(relx=0, rely=0.75, relwidth=0.25, relheight=mvallh)

    label5 = tk.Label(frame5, text="View scan area", bg='white')
    label5.pack()

    root.iconbitmap(r'myicon.ico')
    root.title(f'Sniperbot {version}')

    root.mainloop()
