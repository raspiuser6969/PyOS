menuText = " "
gameMenuText = " "
gameMenuSelect = int(1)
gameMenu = ['   Pong    ','    RPS    ']
menu = [' Power Down','End Program','   Games   ']      #Add Menu Text Here
menuSelect = int(1)
gameMenuSelect = int(1)
x = float(0)
version = "V 0.2"
pix = float(-8)
import RPi.GPIO as GPIO
import sys
import time
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import os
# Input pins:
L_pin = 27
R_pin = 23
C_pin = 4
U_pin = 17
D_pin = 22
A_pin = 5
B_pin = 6
GPIO.setmode(GPIO.BCM)
GPIO.setup(A_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(B_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(L_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(R_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(U_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(D_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(C_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
RST = 24
DC = 23
SPI_PORT = 0
SPI_DEVICE = 0
disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST)
disp.begin()
disp.clear()
disp.display()
width = disp.width
height = disp.height
image = Image.new('1', (width, height))
StartupFont = ImageFont.truetype('upheavtt.ttf', 15)
draw = ImageDraw.Draw(image)
StartupFinishFont = ImageFont.truetype('upheavtt.ttf', 20)
def shutdownApp():                   #App Function (Called in if statement)
    if not GPIO.input(B_pin):
        draw.rectangle((0,0,128,64), outline=0, fill=0)
        disp.image(image)
        disp.display()
        draw.text((8, 32), " SHUTDOWN", font=StartupFinishFont, fill=255)
        disp.image(image)
        disp.display()
        time.sleep(1)
        draw.rectangle((0,0,128,64), outline=0, fill=0)
        disp.image(image)
        disp.display()
        os.system("sudo shutdown -H now")
def stopProg():
    if not GPIO.input(B_pin) :
        draw.rectangle((0,0,128,64), outline=0, fill=0)
        disp.image(image)
        disp.display()
        GPIO.cleanup()
        sys.exit()
def pong():
    draw.text((0,32), "   ERROR   ", )
def rps():
    draw.text((0,32), "   ERROR   ", )
def gameMenuSelect():
    while GPIO.input(A_pin):
        gameMenuText = ""
        draw.rectangle((0,0,128,64), outline=0, fill=0)
        draw.text((0,32), gameMenuText, font=StartupFinishFont, fill=255)
        disp.image(image)
        disp.display()
        if not(GPIO.input(D_pin)):
            gameMenuSelect = gameMenuSelect + 1
            draw.rectangle((0,0,128,64), outline=0, fill=0)
            disp.image(image)
            disp.display()
            print(gameMenuSelect)
        if not(GPIO.input(U_pin)):
            gameMenuSelect = gameMenuSelect - 1
            draw.rectangle((0,0,128,64), outline=0, fill=0)
            disp.image(image)
            disp.display()
            print(gameMenuSelect)
        if gameMenuSelect == 1:                          # Add Menu Items Here.
            gameMenuText = gameMenu[gameMenuSelect - 1]  #
            shutdownApp()                                #
            time.sleep(0.1)                              #
        if gameMenuSelect == 2:                          #
            gameMenuText = gameMenu[gameMenuSelect - 1]  #
            rps()                                        #
            time.sleep(0.1)                              #
        if 2 < gameMenuSelect:
            gameMenuSelect = gameMenuSelect - 1
        if 1 > gameMenuSelect:
            gameMenuSelect = gameMenuSelect + 1
draw.rectangle((0,0,width,height), outline=0, fill=0)
draw.text((8,45),"    PyOS " + version, font=StartupFont, fill=255)
while pix < 113:
    x = x + 1
    x = x * .01
    x = x * 112
    pix = x / 100
    if(pix < 9):
        pix = pix + 8
    else:
        pix = pix + 16
    pix = round(pix, 0)
    draw.rectangle((8,37,120,27), outline=2, fill=0)
    draw.rectangle((8,37,float(pix),27), outline=255, fill=1)
    disp.image(image)
    disp.display()
    print(pix)
draw.rectangle((0,0,128,64), outline=0, fill=0)
draw.text((8,32)," Py OS " + version, font=StartupFinishFont, fill=255)
disp.image(image)
disp.display()
time.sleep(1)
draw.text((8,32)," Main Menu", font=StartupFinishFont, fill=255)
menuIm = Image.open('image.png').resize((128, 64), Image.ANTIALIAS).convert('1')
disp.image(menuIm)
disp.display()
time.sleep(1)
draw.rectangle((0,0,128,64), outline=0, fill=0)
while 1:
    draw.text((0,32), menuText, font=StartupFinishFont, fill=255)
    disp.image(image)
    disp.display()
    if not(GPIO.input(D_pin)):
        menuSelect = menuSelect + 1
        draw.rectangle((0,0,128,64), outline=0, fill=0)
        disp.image(image)
        disp.display()
        print(menuSelect)
    if not(GPIO.input(U_pin)):
        menuSelect = menuSelect - 1
        draw.rectangle((0,0,128,64), outline=0, fill=0)
        disp.image(image)
        disp.display()
        print(menuSelect)
    if menuSelect == 1:                      # Add Menu Items Here.
        menuText = menu[menuSelect - 1]      #
        shutdownApp()                        #
        time.sleep(0.1)                      #
    if menuSelect == 2:                      #
        menuText = menu[menuSelect - 1]      #
        stopProg()                           #
        time.sleep(0.1)                      #
    if menuSelect == 3:
        menuText = menu[menuSelect - 1]
        gameMenuSelect()
        time.sleep(0.1)
    if 3 < menuSelect:
        menuSelect = menuSelect - 1
    if 1 > menuSelect:
        menuSelect = menuSelect + 1
