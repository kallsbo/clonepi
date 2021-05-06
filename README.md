# ClonePi Project
Using a Raspberry Pi with an LCD keypad HAT to image new SD-cards for Raspberry Pi projects without the need for a computer. Images are kept on a USB stick and you simply insert an SD-card and select the image in the list and then wait for it to image.

## Installation
sudo apt-get update  
sudo apt-get install git python3-pip  

sudo raspi-config  
3 - Interface options  
P5 I2C  

sudo pip3 install RPi.GPIO  
sudo pip3 install Adafruit_CharLCD  

git clone https://github.com/kallsbo/clonepi.git
