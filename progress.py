#!/usr/bin/python3
import sys
import Adafruit_CharLCD as LCD

# Setup screen
lcd = LCD.Adafruit_CharLCDPlate()
lcd.set_color(0.0, 0.0, 0.0)
lcd.clear()

lcd.message(sys.argv[1])
