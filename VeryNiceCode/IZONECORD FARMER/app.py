import pyautogui
import PIL
import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
from PIL import Image
import PIL.ImageGrab
import time
import datetime
import string
from PIL import ImageTk
from configparser import ConfigParser
import schedule
#disclaimer: this code is very bad

cfile = r'config.ini'
config = ConfigParser()
config.read(cfile)

#Premade Time

izcord_s = config['Premade Times']['izcord_s']
izcord_s = izcord_s.split(" ")
izcord_e = config['Premade Times']['izcord_e']
izcord_e = izcord_e.split(" ")

def updated_time():
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    return current_time.split(':')

def tti(): #tti stands for text to image kekw
    stoplist = []
    stoplist = izcord_e

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
                tti()
            else:
                text = ''.join(lz[0:4])
                text = text.upper()
                pyautogui.click(426,1008)
                pyautogui.typewrite(f'!claim {text}')
                pyautogui.hotkey('enter')
                print('Mission Success we got em bois')
                print(text)
                time.sleep(60)
                print("Waiting on next drop")
                
        except:
            tti()

schedule.every().hour.at(f":{izcord_s[0]}").do(tti)
schedule.every().hour.at(f":{izcord_s[1]}").do(tti)
schedule.every().hour.at(f":{izcord_s[2]}").do(tti)
schedule.every().hour.at(f":{izcord_s[3]}").do(tti)
schedule.every().hour.at(f":{izcord_s[4]}").do(tti)
schedule.every().hour.at(f":{izcord_s[5]}").do(tti)
schedule.every().hour.at(f":{izcord_s[6]}").do(tti)
schedule.every().hour.at(f":{izcord_s[7]}").do(tti)

while True:
    current_time = updated_time()
    print('Cycling for IZ*ONECord: ' + ":".join(current_time))
    schedule.run_pending()
    time.sleep(1)