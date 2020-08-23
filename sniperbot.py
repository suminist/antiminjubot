import numpy as np
from numpy import save, load
import sys
import schedule
from configparser import ConfigParser
from pynput.keyboard import Listener, KeyCode
import PIL
import PIL.ImageGrab
from PIL import Image, ImageEnhance, ImageOps, ImageFilter, ImageChops
from PIL import ImageTk
import os
from pathlib import Path
import string
import datetime
import time
import tkinter as tk
from tkinter import OptionMenu, StringVar
import pyautogui
import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

np.set_printoptions(threshold=sys.maxsize)

x1 = 450
x2 = 510
y1 = 934
y2 = 949

cfile = r'VeryNiceCode/config.ini'
config = ConfigParser()
config.read(cfile)

#Premade Time

wkcord_s = config['Premade Times']['wkcord_s']
wkcord_s = wkcord_s.split(" ")
wkcord_e = config['Premade Times']['wkcord_e']
wkcord_e = wkcord_e.split(" ")

izcord_s = config['Premade Times']['izcord_s']
izcord_s = izcord_s.split(" ")
izcord_e = config['Premade Times']['izcord_e']
izcord_e = izcord_e.split(" ")

#Custom Time
custom_s = config['Custom Time']['custom_s']
custom_s = custom_s.split(" ")
custom_e = config['Custom Time']['custom_e']
custom_e = custom_e.split(" ")


def updated_time():
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    return current_time.split(':')


class Sniperbot:
    def __init__(self, cord):
        self.cord = cord

    def tti(self):  # tti stands for text to image kekw
        stoplist = []
        if self.cord == 'weeekly':
            stoplist = wkcord_e

        elif self.cord == 'iz*one':
            stoplist = izcord_e

        elif self.cord == 'custom':
            stoplist = custom_e

        current_time = updated_time()

        if current_time[1] in stoplist:
            print('Awaiting next drop')
        else:
            
            ########## RASMIT CODE HERE

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
                return tti()

            temp_prefix = "F9Y8"

            for i in range(4):
                code += read(immatrixTsplit[2 * i], i)

            print(code)

            pyautogui.click(950, 1007)
            pyautogui.typewrite('!claim ' + code)
            pyautogui.hotkey('enter')

            endTime = time.time()
            print("End Time: " + str(endTime))

            print("Elapsed Time: " + str(endTime - startTime) + " seconds")

            ########## RASMIT CODE HERE

def read(matrix, index):
    if (index == 0 or index == 2):
        characters = ["A", "B", "C", "D", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q",
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

def viewimg():
    im = PIL.ImageGrab.grab(bbox=(447, 933, 510, 953))  # X1,Y1,X2,Y2
    custom_config = r'--oem 3 --psm 7'
    text = tess.image_to_string(im, config=custom_config)
    print("Scanned Text: " + text.strip())
    im.show()


def clock():
    hour = time.strftime("%H")
    minute = time.strftime("%M")
    second = time.strftime("%S")

    lclock.config(text=f"{hour}:{minute}:{second}")
    lclock.after(1000, clock)


def startbot():
    print(izcord_s[0])


def showcord(event):
    scord = cord.get()
    label2.config(text=f"Selected Target: {cord.get()}")
    if scord == "Weeekly":
        label2x.config(text="Start: " + " | ".join(wkcord_s))
        label2y.config(text="End: " + " | ".join(wkcord_e))
        # label2z.config(text=f"Start:{wkcord_ss} End:{wkcord_ee}")
        button.config(command=wkstart)
        print("Set to WeeeklyCord")
    elif scord == "IZ*ONE":
        label2x.config(text="Start: " + " | ".join(izcord_s))
        label2y.config(text="End: " + " | ".join(izcord_e))
        # label2z.config(text=f"Start:{izcord_ss} End:{izcord_ee}")
        button.config(command=izstart)
        print("Set to IZ*ONECord")
    elif scord == "Custom Time":
        label2x.config(text="Start: " + " | ".join(custom_s))
        label2y.config(text="End: " + " | ".join(custom_e))
        # label2z.config(text=f"Start:{custom_ss} End:{custom_ee}")
        button.config(command=custart)
        print("Set to Custom Cord")
    elif scord == "None":
        label2x.config(text="No start times selected")
        label2y.config(text="No end times selected")
        # label2z.config(text="No Specific time selected")
        button.config(command=startbot)
        print("Set to None")


def izs():
    schedule.every().hour.at(f":{izcord_s[0]}").do(Sniperbot('iz*one').tti)
    schedule.every().hour.at(f":{izcord_s[1]}").do(Sniperbot('iz*one').tti)
    schedule.every().hour.at(f":{izcord_s[2]}").do(Sniperbot('iz*one').tti)
    schedule.every().hour.at(f":{izcord_s[3]}").do(Sniperbot('iz*one').tti)
    schedule.every().hour.at(f":{izcord_s[4]}").do(Sniperbot('iz*one').tti)
    schedule.every().hour.at(f":{izcord_s[5]}").do(Sniperbot('iz*one').tti)
    schedule.every().hour.at(f":{izcord_s[6]}").do(Sniperbot('iz*one').tti)
    schedule.every().hour.at(f":{izcord_s[7]}").do(Sniperbot('iz*one').tti)

    current_time = updated_time()
    print('Cycling for IZ*ONECord: ' + ":".join(current_time))
    time.sleep(1)
    return schedule.run_pending()


def izstart():
    izs()
    while True:
        time.sleep(1)
        current_time = updated_time()
        print('Cycling for IZ*ONECord: ' + ":".join(current_time))
        schedule.run_pending()


def wks():
    schedule.every().hour.at(f":{wkcord_s[0]}").do(Sniperbot('weeekly').tti())
    schedule.every().hour.at(f":{wkcord_s[1]}").do(Sniperbot('weeekly').tti())
    schedule.every().hour.at(f":{wkcord_s[2]}").do(Sniperbot('weeekly').tti())
    schedule.every().hour.at(f":{wkcord_s[3]}").do(Sniperbot('weeekly').tti())

    current_time = updated_time()
    print('Cycling for WeeeklyCord: ' + str(current_time))
    time.sleep(1)
    return schedule.run_pending()


def wkstart():
    wks()
    while True:
        time.sleep(1)
        current_time = updated_time()
        print('Cycling for WeeeklyCord: ' + ":".join(current_time))
        schedule.run_pending()


def cus():
    schedule.every().hour.at(":51").do(Sniperbot('custom').tti())
    schedule.every().hour.at(":51").do(Sniperbot('custom').tti())
    schedule.every().hour.at(":51").do(Sniperbot('custom').tti())
    schedule.every().hour.at(":51").do(Sniperbot('custom').tti())
    schedule.every().hour.at(":51").do(Sniperbot('custom').tti())
    schedule.every().hour.at(":51").do(Sniperbot('custom').tti())
    schedule.every().hour.at(":51").do(Sniperbot('custom').tti())
    schedule.every().hour.at(":51").do(Sniperbot('custom').tti())

    current_time = updated_time()
    print('Cycling for Custom: ' + str(current_time))
    time.sleep(1)
    return schedule.run_pending()


def custart():
    cus()
    while True:
        time.sleep(1)
        current_time = updated_time()
        print('Cycling for Custom Times: ' + ":".join(current_time))
        schedule.run_pending()


ht = 400
wd = 596
mvall = 0.5
mvallh = 0.25

version = 'SYBot V.2.3.1-a.2'

root = tk.Tk()
#main canvas
canvas = tk.Canvas(root, height=ht, width=wd)
canvas.pack()
#background image
background_img = ImageTk.PhotoImage(Image.open(r'32.png'))
background_label = tk.Label(root, image=background_img)
background_label.place(relx=0.5, rely=0.25, relwidth=mvall, relheight=0.5)
#main frame
#relx, rely in percentages
frame = tk.Frame(root, bg='black')
frame.place(relx=0, rely=0, relwidth=1, relheight=0.25)

label = tk.Label(frame, text='Starts bot instantly', bg='black', fg='pink')
label.pack()

cord = StringVar()
cord.set("None")

drop = OptionMenu(frame, cord, "None", "Weeekly", "IZ*ONE",
                  "Custom Time", command=showcord)
drop.pack()

button = tk.Button(frame, text="Start Bot", bg='black',
                   fg='pink', command=startbot)
button.pack(side='bottom')

#frame 2
frame2 = tk.Frame(root, bg='black')
frame2.place(relx=0, rely=0.25, relwidth=mvall, relheight=0.5)

#cord name
label2 = tk.Label(frame2, text="Selected Cord: None", font=(
    "Helvetica", 10), bg='black', fg='#add8e6')
label2.pack()
#start times
label2x = tk.Label(frame2, text="Start times: None", bg='black', fg='pink')
label2x.pack()
#end times
label2y = tk.Label(frame2, text="End times: None", bg='black', fg='pink')
label2y.pack()
#specific seconds
# label2z = tk.Label(frame2, text="Specific times: None", bg='black', fg='pink')
# label2z.pack()

#frame 4
frame4 = tk.Frame(root, bg='black')
frame4.place(relx=0.5, rely=0.75, relwidth=mvall, relheight=mvallh)

label4 = tk.Label(frame4, text="View scan area", bg='black', fg='pink')
label4.pack()

# lambda:[funcA(), funcB(), funcC()])
button4 = tk.Button(frame4, text="View area", bg='black',
                    fg='pink', command=viewimg)
button4.pack(side='bottom')

frame5 = tk.Frame(root, bg='black')
frame5.place(relx=0, rely=0.75, relwidth=mvall, relheight=mvallh)
#custom clock
lclock = tk.Label(frame5, text="", font=(
    "Helvetica", 32), fg="pink", bg="black")
lclock.pack(pady=20)
clock()

isrunning = tk.Label(frame2, text="Status check (will fix when 3.0 comes out)", font=(
    "Helvetica", 10), bg="black", fg="#add8e6")
isrunning.pack()
is2 = tk.Label(frame2, text="", bg="black", fg="pink")
is2.pack()

root.iconbitmap(r'myicon.ico')
root.title(f'Sniperbot {version}')

root.mainloop()
