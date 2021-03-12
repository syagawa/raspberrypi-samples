# sudo apt install python3-pip
# sudo pip3 install Adafruit-Blinka
# sudo python -m pip install --upgrade pip setuptools wheel
# sudo pip install Adafruit-SSD1306
# sudo raspi-config
#  => Interface Options I2C enable


import time

import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

import subprocess


RST = None
DC = 23
SPI_PORT = 0
SPI_DEVICE = 0

d = Adafruit_SSD1306.SSD1306_128_64(rst=RST)

d.begin()
d.clear()
d.display()

w = d.width
h = d.height
image = Image.new("1", (w, h))
draw.ImageDraw(image)

def drawBlackRect():
  draw.rectangle((0, 0, w, h), outline=0, fill=0)

drawBlackRect()

pad = -2
top = pad
bottom = h - pad

x = 0

font = ImageFont.load_default()

while True:
  drawBlackRect()

  draw.text( (x, top), "AAAA")

  d.image(image)
  d.display()
  time.sleep(0.1)