import tkinter as tk
from tkinter import OptionMenu, StringVar
import pyautogui
import PIL
import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
from PIL import Image, ImageEnhance, ImageOps, ImageFilter, ImageChops
import PIL.ImageGrab
import time
import datetime
import string
from pathlib import Path
import os
from PIL import ImageTk
from pynput.keyboard import Listener, KeyCode
from configparser import ConfigParser

#disclaimer: this code is very bad

cfile = r'config.ini'
config = ConfigParser()
config.read(cfile)

#Premade Times
wkcord_s = config['Premade Times']['wkcord_s']
wkcord_s = wkcord_s.split(" ")
wkcord_e = config['Premade Times']['wkcord_e']
wkcord_e = wkcord_e.split(" ")

izcord_s = config['Premade Times']['izcord_s']
izcord_s = izcord_s.split(" ")
izcord_e = config['Premade Times']['izcord_e']
izcord_e = izcord_e.split(" ")
#Specific Premade times
wkcord_ss = config['Premade Times']['wkcord_ss']
wkcord_ss = int(wkcord_ss)
wkcord_ee = config['Premade Times']['wkcord_ee']
wkcord_ee = int(wkcord_ee)

izcord_ss = config['Premade Times']['izcord_ss']
izcord_ss = int(izcord_ss)
izcord_ee = config['Premade Times']['izcord_ee']
izcord_ee = int(izcord_ee)
#Custom Time
custom_s = config['Custom Time']['custom_s']
custom_s = custom_s.split(" ")
custom_e = config['Custom Time']['custom_e']
custom_e = custom_e.split(" ")
#Specific Custom Time
custom_ss = config['Custom Time']['custom_ss']
custom_ss = int(custom_ss)
custom_ee = config['Custom Time']['custom_ee']
custom_ee = int(custom_ee)


class Sniperbot:

    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    current_time = current_time.split(':')
    def __init__(self, ss, cord):
        self.cord = cord
        self.ss = ss
        
    def timecheck(self):
        if self.cord.lower() == 'weeekly':
            startlist = wkcord_s
        elif self.cord.lower() == 'iz*one':
            startlist = izcord_s
        elif self.cord.lower() == 'custom_s':
            startlist = custom_s
        
        if self.ss == 'wkcord_ss':
            sstime = wkcord_ss
        elif self.ss == 'izcord_ss':
            sstime = izcord_ss
        elif self.ss == 'custom_ss':
            sstime = custom_ss

        if self.current_time[2] < sstime:
            if Sniperbot.current_time[1] in startlist:
                print('Bot commencing')
                self.tti()
        else:
            print(f'cycling via SStime: {Sniperbot.current_time[0]}:{Sniperbot.current_time[1]} - WeeklyCord')
            time.sleep(10)
            self.timecheck()

    def tti(self): #tti stands for text to image kekw
        if self.cord == 'weeekly':
            stoplist = wkcord_e
        elif self.cord == 'iz*one':
            stoplist = izcord_e
        elif self.cord == 'custom_e':
            stoplist = custom_e

        if self.ss == 'wkcord_ee':
            sstime = wkcord_ee
        elif self.ss == 'izcord_ee':
            sstime = izcord_ee
        elif self.ss == 'custom_ee':
            sstime = custom_ee
        
        if self.current_time[2] > sstime or sstime == 0:
            if Sniperbot.current_time[1] in stoplist:
                print('it is not time yet')
                self.timecheck()
            else:
                im = PIL.ImageGrab.grab(bbox=(902,813, 1016,860))  # X1,Y1,X2,Y2
                custom_config = r'--oem 3 --psm 7'
                text = tess.image_to_string(im, config=custom_config)
                ''.join(e for e in text if e.isalnum())
                lz = list(text)
                try:
                    if lz[0] == 'j':
                        lz.remove(''.join(lz[0]))
                    if lz[3].lower() == 'o':
                        lz[3] = '0'
                        print('modified 1')
                    if lz[1].lower() == 'o':
                        lz[1] = '0'
                        print('modified 2')
                    if lz[3].lower() == 'i':
                        lz[3] = '9'
                        print('modified 3')
                    if lz[1].lower() == 's':
                        lz[1] = '9'
                        print('modified 4')
                    if lz[3].lower() == 's':
                        lz[3] = '8'
                        print('modified 5')
                    if lz[1].lower() == 'i':
                        lz[1] = '1'
                        print('modified 6')
                    if lz[2] == '6':
                        lz[2] = 'G'
                        print('modified 6x')
                    if lz[2].islower() == True:
                        lz.remove(''.join(lz[2]))
                        print('modified 7')
                    if lz[0] == '5':
                        lz[0] = 'T'
                        print('modified 8')
                    if lz[2] == '3':
                        lz[2] = 'H'
                        print('modified 9')
                    if lz[0] == '0':
                        lz[0] = 'O'
                        print('modified 10')
                    if lz[2] == '0':
                        lz[2] = 'O'
                        print('modified 11')
                except:
                    pass
                try:
                    if lz[0].isalpha == False or lz[1].isnumeric() == False or lz[1] == 'l' or lz[3].isnumeric() == False:
                        print(lz)
                        tti()
                    else:
                        text = ''.join(lz[0:4])
                        text = text.upper()
                        pyautogui.typewrite(f'!claim {text}')
                        pyautogui.hotkey('enter')
                        print('Mission Success we got em bois')
                        print(text)
                        isrunning.config(text="Timecheck Phase 2")
                        isrunning.after(2000, self.timecheck())
                except:
                    self.tti()
        else:
            self.timecheck()

def startbot():
    bot = Sniperbot(0, 'weeekly')
    bot.timecheck()

def viewimg():
    im = PIL.ImageGrab.grab(bbox=(902,813, 1016,860))  # X1,Y1,X2,Y2
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

ht = 400
wd = 596
mvall = 0.5
mvallh = 0.25
root = tk.Tk()

version = 'SYBot V.2.1.1-a.1'

#main canvas
canvas = tk.Canvas(root, height=ht,width=wd)
canvas.pack()
#background image
background_img = ImageTk.PhotoImage(Image.open(r'32.png'))
background_label = tk.Label(root, image=background_img)
background_label.place(relx=0.5,rely=0.25,relwidth=mvall,relheight=0.5)
#main frame
#relx, rely in percentages
frame = tk.Frame(root, bg='black')
frame.place(relx=0, rely=0, relwidth=1, relheight=0.25)

label = tk.Label(frame, text='Starts bot instantly', bg='black', fg='pink')
label.pack()

cord = StringVar()
cord.set("Weeekly")

drop = OptionMenu(frame, cord, "Weeekly", "IZ*ONE", "Custom Time")
drop.pack()

button = tk.Button(frame, text="Start Bot", bg='black', fg='pink', command=startbot)
button.pack(side='bottom')

#frame 2
frame2 = tk.Frame(root, bg='black')
frame2.place(relx=0, rely=0.25, relwidth=mvall, relheight=0.5)

label2 = tk.Label(frame2, text="WeeeklyCord",font=("Helvetica", 10), bg='black', fg='#add8e6')
label2.pack()

label2x = tk.Label(frame2, text=" | ".join(wkcord_s), bg='black', fg='pink')
label2x.pack()

label2x = tk.Label(frame2, text="IZ*ONECord",font=("Helvetica", 10), bg='black', fg='#add8e6')
label2x.pack()

label2x = tk.Label(frame2, text=" | ".join(wkcord_e), bg='black', fg='pink')
label2x.pack()

#frame 4
frame4 = tk.Frame(root, bg='black')
frame4.place(relx=0.5,rely=0.75,relwidth=mvall,relheight=mvallh)

label4 = tk.Label(frame4, text="View scan area", bg='black', fg='pink')
label4.pack()

button4 = tk.Button(frame4, text="View area", bg='black', fg='pink', command=viewimg)#lambda:[funcA(), funcB(), funcC()])
button4.pack(side='bottom')

frame5 = tk.Frame(root, bg='black')
frame5.place(relx=0, rely=0.75, relwidth=mvall, relheight=mvallh)
#custom clock
lclock = tk.Label(frame5, text="", font=("Helvetica", 32), fg="pink", bg="black")
lclock.pack(pady=20)
clock()

isrunning = tk.Label(frame2, text="Isitrunning?",font=("Helvetica", 10), bg="black", fg="#add8e6")
isrunning.pack()
isrunning = tk.Label(frame2, text="", bg="black", fg="pink")
isrunning.pack()

root.iconbitmap(r'myicon.ico')
root.title(f'Sniperbot {version}')

root.mainloop()

