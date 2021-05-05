#!/usr/bin/python
from time import sleep
import os
import glob
import ntpath
import Adafruit_CharLCD as LCD

# SETTINGS
imgsrc = "/mnt/usbstick"

# ENDSETTINGS

# Get images
images = [f for f in glob.glob(imgsrc + "/*.img")]

# Setup screen
lcd = LCD.Adafruit_CharLCDPlate()
lcd.set_color(0.0, 0.0, 0.0)
lcd.clear()

# State
state = 0
imgSel = 0

try:
    while True:
        if state == 0 and imgSel == 0:
            lcd.home()
            lcd.message("Select img (" + str(len(images)) + ")  ")

        # If image selecting scroll the name across he screen
        if state == 0 and imgSel > 0:
            lcd.move_left()
            sleep(0.35)

        # Capture image select
        if lcd.is_pressed(LCD.DOWN):
            if imgSel + 1 <= len(images):
                imgSel += 1
            else:
                imgSel = 0
            lcd.clear()
            lcd.message(ntpath.basename(images[imgSel - 1]) + " ")
        if lcd.is_pressed(LCD.UP):
            if imgSel - 1 >= 0:
                imgSel -= 1
            else:
                imgSel = len(images)
            lcd.clear()
            lcd.message(ntpath.basename(images[imgSel - 1]) + " ")

        # Capture selection
        if lcd.is_pressed(LCD.SELECT) and state == 0 and imgSel > 0:
            state = 1
            lcd.clear()
            lcd.message("Write image?")
            lcd.message("\nLFT=CANC  SEL=OK")
        # Capture cancel
        if lcd.is_pressed(LCD.LEFT) and state == 1:
            lcd.clear()
            state = 0
            imgSel = 0
        # Capture write confirmation
        if lcd.is_pressed(LCD.SELECT) and state == 1:
            lcd.clear()
            state = 2
            # Write image
            #os.system("bash -c \"(pv -f --width 16 -p {0} | sudo dd of=/dev/sdb) |& stdbuf -oL tr '\r' '\n' | (while read -r LINE; do python3 progress.py '$LINE'; done;)\"".format(images[imgSel -1]))
            os.system("bash -c '(pv -f --width 16 -p {0} | sudo dd of=/dev/sdb) |& stdbuf -oL tr '\\''\r'\\'' '\\''\n'\\'' | (while read -r LINE; do python3 progress.py \"$LINE\"; done;)'".format(images[imgSel -1]))
            # Signal ready
            state = 3
            lcd.clear()
            lcd.message("SD WRITE DONE!")
            lcd.message("\nSEL=OK")
            lcd.set_color(0,100,0)
        # Capture reset
        if lcd.is_pressed(LCD.SELECT) and state == 3:
            lcd.clear()
            lcd.set_color(0,0,0)
            imgSel = 0
            state = 0

except KeyboardInterrupt:
    pass
finally:
    lcd.clear()

