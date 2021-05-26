import pyautogui
import pytesseract as tess
import PIL
from PIL import Image, ImageEnhance, ImageOps, ImageFilter, ImageChops
import PIL.ImageGrab
import time
import datetime
import string

tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

stoplist = ['08','23', '38', '53']

# part of the screen
def tti():
    while True:
        t = time.localtime()
        current_time = time.strftime("%H:%M:%S", t)
        current_time = current_time.split(':')

        if current_time[1] in stoplist:
            print('it is not time yet')
            timecheck()
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
                    tti()
                else:
                    text = ''.join(lz[0:4])
                    text = text.upper()

                    pyautogui.typewrite(f'!claim {text}')
                    pyautogui.hotkey('enter')
                    time.sleep(2)

                    print('Mission Success we got em bois')
                    print(text)
                    timecheck()
            except:
                tti()
                

def timecheck():
    while True:
        snipelist = ['07','22', '37', '52']

        t = time.localtime()
        current_time = time.strftime("%H:%M:%S", t)
        current_time = current_time.split(':')

        print(current_time)

        restartlist = ['49', '50']

        if current_time[1] in restartlist:
            break
        else:
            if current_time[1] in snipelist:
                print('mission commence')

                tti()
            else:
                print(f'cycling: {current_time[1]}')

                time.sleep(10)
                timecheck()

timecheck()
