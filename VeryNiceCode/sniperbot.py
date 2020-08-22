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
import schedule
#disclaimer: this code is very bad

cfile = r'config.ini'
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

    def tti(self): #tti stands for text to image kekw
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
            im = PIL.ImageGrab.grab(bbox=(447,933, 510,953))  # X1,Y1,X2,Y2
            custom_config = r'--oem 3 --psm 7'
            text = tess.image_to_string(im, config=custom_config)
            ''.join(e for e in text if e.isalnum())
            lz = list(text)
            try:
                # [0] = Alpha
                # [1] = Numerical
                # [2] = Alpha
                # [3] = Numerical
                #Alpha
                if lz[0] == '5':
                    lz[0] = 'T'
                if lz[0] == 'j':
                    lz.remove(''.join(lz[0]))
                if lz[0] == '0':
                    lz[0] = 'O'        
                #Numerical
                if lz[1].lower() == 'o':
                    lz[1] = '0'
                if lz[1].lower() == 's':
                    lz[1] = '9'
                if lz[1].lower() == 'i':
                    lz[1] = '1'
                #Alpha
                if lz[2].islower() == True:
                    lz.remove(''.join(lz[2]))
                    print('modified 7')
                if lz[2] == '6':
                    lz[2] = 'G'
                    print('modified 6x')
                if lz[2] == '3':
                    lz[2] = 'H'
                    print('modified 9')
                if lz[2] == '0':
                    lz[2] = 'O'
                    print('modified 11')

                #Numerical
                if lz[3].lower() == 'o':
                    lz[3] = '0'
                if lz[3].lower() == 'i':
                    lz[3] = '9'
                if lz[3].lower() == 's':
                    lz[3] = '8'
            except:
                pass
            try:
                if lz[0].isalpha == False or lz[1].isnumeric() == False or lz[1] == 'l' or lz[3].isnumeric() == False:
                    print(lz)
                    self.tti()
                else:
                    text = ''.join(lz[0:4])
                    text = text.upper()
                    pyautogui.typewrite(f'!claim {text}')
                    pyautogui.hotkey('enter')
                    print('Mission Success we got em bois')
                    print(text) 
                    time.sleep(60)
                    print("Waiting on next drop")
            except:
                self.tti()

def viewimg():
    im = PIL.ImageGrab.grab(bbox=(447,933, 510,953))  # X1,Y1,X2,Y2
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
    schedule.every().hour.at(f":{izcord_s[0]}").do(Sniperbot('iz*one').tti())
    schedule.every().hour.at(f":{izcord_s[1]}").do(Sniperbot('iz*one').tti())
    schedule.every().hour.at(f":{izcord_s[2]}").do(Sniperbot('iz*one').tti())
    schedule.every().hour.at(f":{izcord_s[3]}").do(Sniperbot('iz*one').tti())
    schedule.every().hour.at(f":{izcord_s[4]}").do(Sniperbot('iz*one').tti())
    schedule.every().hour.at(f":{izcord_s[5]}").do(Sniperbot('iz*one').tti())
    schedule.every().hour.at(f":{izcord_s[6]}").do(Sniperbot('iz*one').tti())
    schedule.every().hour.at(f":{izcord_s[7]}").do(Sniperbot('iz*one').tti())

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
cord.set("None")

drop = OptionMenu(frame, cord,"None", "Weeekly", "IZ*ONE", "Custom Time", command=showcord)
drop.pack()

button = tk.Button(frame, text="Start Bot", bg='black', fg='pink', command=startbot)
button.pack(side='bottom')

#frame 2
frame2 = tk.Frame(root, bg='black')
frame2.place(relx=0, rely=0.25, relwidth=mvall, relheight=0.5)

#cord name
label2 = tk.Label(frame2, text="Selected Cord: None",font=("Helvetica", 10), bg='black', fg='#add8e6')
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

isrunning = tk.Label(frame2, text="Status check (will fix when 3.0 comes out)",font=("Helvetica", 10), bg="black", fg="#add8e6")
isrunning.pack()
is2 = tk.Label(frame2, text="", bg="black", fg="pink")
is2.pack()

root.iconbitmap(r'myicon.ico')
root.title(f'Sniperbot {version}')

root.mainloop()

