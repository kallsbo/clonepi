# clonepi
Scripts for the ClonePi project. Imaging SD-cards from a Raspberry Pi directly controlled with a keypad and an LCD 16x2 screen.

## PRE-REQS

sudo apt-get update
sudo apt-get install git build-essential python3-dev python3-smbus python3-pip

## Adafruit CharLCD
sudo pip3 install RPi.GPIO
cd ~
git clone https://github.com/adafruit/Adafruit_Python_CharLCD.git
cd Adafruit_Python_CharLCD
sudo python3 setup.py install
