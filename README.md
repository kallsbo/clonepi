# ClonePi Project
![ClonePi in action](https://github.com/kallsbo/clonepi/raw/main/clonepi.jpg)
Using a Raspberry Pi with an LCD keypad HAT to image new SD-cards for Raspberry Pi projects without the need for a computer. Images are kept on a USB stick and you simply insert an SD-card and select the image in the list and then wait for it to image.

## Installation
```bash
sudo apt-get update  
sudo apt-get install git python3-pip  
```
Enable the I2C interface from Raspi-Config
```bash
sudo raspi-config  
```
Select option **3 - Interface options**  
Then option **P5 I2C**  

```bash
sudo pip3 install RPi.GPIO  
sudo pip3 install Adafruit_CharLCD  
git clone https://github.com/kallsbo/clonepi.git
```

## Operation
Don't start the ClonePi with both an SD-card reader/writer and the USB-stick/drive connected. Then it will be hard to know which one is which when mounting. Make sure to mount the USB-stick/drive to **/mnt/usbstick** or change the **imgsrc** setting in **main.py**.  

Then run the main script
```bash
python3 main.py
```
This will display the **Select image (x)** screen on the LCD. Then use the **UP** and **DOWN** buttons to select the image you would like to image. Insert an SD-card reader/writer containing the destination card. Press **SELECT** and confirm the write. Now the image will write to the SD-card.

## Room for improvments and conclusions
There are several things that can be improved on this quick and dirty project.
* Error handeling
* Autostart
* Nice case

This was a quick and dirty project to actually use the HAT that was in my scrap bin. What ever you do don't do this on a Raspberry Pi 1, it's really slow.
