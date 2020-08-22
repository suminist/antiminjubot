import tkinter as tk
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

def tti2():
    stoplist = ['05', '13', '20', '28', '35', '43','50','58']
    while True:
        t = time.localtime()
        current_time = time.strftime("%H:%M:%S", t)
        current_time = current_time.split(':')
        if current_time[1] in stoplist:
            print('it is not time yet')
            timecheck2()
        else:
            im = PIL.ImageGrab.grab(bbox=(447,933, 510,953))  # X1,Y1,X2,Y2
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
                    tti2()
                else:
                    text = ''.join(lz[0:4])
                    text = text.upper()
                    pyautogui.typewrite(f'!claim {text}')
                    pyautogui.hotkey('enter')
                    time.sleep(2)
                    print('Mission Success we got em bois')
                    print(text)
                    timecheck2()
            except:
                tti2()

def timecheck2():
    snipelist = ['04', '12', '19', '27', '34', '42','49','57']
    while True:
        t = time.localtime()
        current_time = time.strftime("%H:%M:%S", t)
        current_time = current_time.split(':')
        if current_time[1] == '50':
            print('Stopping bot to prevent crash')
            break
        elif current_time[1] in snipelist:
            label['text'] = 'Bot commencing'
            tti2()
        else:
            print(f'cycling: {current_time[0]}:{current_time[1]} - IZ*ONECord')
            time.sleep(10)
            timecheck2()

def ttinstant():
    im = PIL.ImageGrab.grab(bbox=(447,933, 510,953))  # X1,Y1,X2,Y2
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
            time.sleep(2)
            print('Mission Success we got em bois')
            print(text)
    except:
        tti()

def viewimg():
    im = PIL.ImageGrab.grab(bbox=(447,933, 510,953))  # X1,Y1,X2,Y2
    custom_config = r'--oem 3 --psm 7'
    text = tess.image_to_string(im, config=custom_config)
    print("Scanned Text: "+text.strip())
    im.show()

ht = 360
wd = 600
mvall = 0.5
mvallh = 0.25
root = tk.Tk()

version = 'SYBot V.2.1.0-a.1'

#main canvas
canvas = tk.Canvas(root, height=ht,width=wd)
canvas.pack()
#background image
background_img = ImageTk.PhotoImage(Image.open(r'32.png'))
background_label = tk.Label(root, image=background_img)
background_label.place(relx=0.5,rely=0.25,relwidth=mvall,relheight=0.5)
#main frame
#relx, rely in percentages
frame = tk.Frame(root, bg='pink')
frame.place(relx=0, rely=0, relwidth=1, relheight=0.25)

label = tk.Label(frame, text='Starts bot instantly', bg='white')
label.pack()

button = tk.Button(frame, text="Start Bot", bg='#50A7AB', fg='#000000', command=ttinstant)
button.pack(side='bottom')

#frame 2
frame2 = tk.Frame(root, bg='#92F1FE')
frame2.place(relx=0, rely=0.25, relwidth=mvall, relheight=mvallh)

label2 = tk.Label(frame2, text="WeeeklyCord", bg='white')
label2.pack()
label2x = tk.Label(frame2, text="12 | 27 | 42 | 57", bg='white')
label2x.pack()

button2 = tk.Button(frame2, text="Start Bot", bg='#50A7AB', fg='#000000', command=timecheck)
button2.pack(side='bottom')

#frame 3
frame3 = tk.Frame(root, bg='#F69AF8')
frame3.place(relx=0,rely=0.5,relwidth=mvall,relheight=mvallh)

label3 = tk.Label(frame3, text="IZ*ONECord", bg='white')
label3.pack()
label3x= tk.Label(frame3, text="04 | 12 | 19 | 27 | 34 | 42 | 49 | 57", bg="white")
label3x.pack()

button3 = tk.Button(frame3, text="Start Bot", bg='#50A7AB', fg='#000000', command=timecheck2)
button3.pack(side='bottom')

#frame 4
frame4 = tk.Frame(root, bg='#E2F89A')
frame4.place(relx=0.25,rely=0.75,relwidth=mvall,relheight=mvallh)

label4 = tk.Label(frame4, text="View scan area", bg='white')
label4.pack()

button4 = tk.Button(frame4, text="View area", bg='#50A7AB', fg='#000000', command=viewimg)
button4.pack(side='bottom')

#frame 5
frame5 = tk.Frame(root, bg='#E2F89A')
frame5.place(relx=0,rely=0.75,relwidth=0.25,relheight=mvallh)

label5 = tk.Label(frame5, text="View scan area", bg='white')
label5.pack()

root.iconbitmap(r'myicon.ico')
root.title(f'Sniperbot {version}')

root.mainloop()

