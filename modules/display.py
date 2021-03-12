# sudo apt install python3-pip
# sudo pip3 install Adafruit-Blinka
# sudo pip3 install adafruit-circuitpython-ssd1306
# sudo apt install python3-pil

import time
import subprocess

import board
import digitalio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306

display_reset = digitalio.DigitalInOut(board.D4)

w = 128
h = 64

I2C = board.I2C()
d = adafruit_ssd1306.SSD1306_I2C(w, h, I2C, addr=0x3C, reset=display_reset)

d.fill(0)

d.show()


image = Image.new("1", (d.width, d.height))
draw = ImageDraw.Draw(image)

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

  draw.text( (x, top), "AAAA", font=font, fill=255)

  d.image(image)
  d.show()
  time.sleep(0.1)
  print("loop")