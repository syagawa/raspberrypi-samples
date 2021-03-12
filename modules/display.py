# sudo apt install python3-pip
# sudo pip3 install Adafruit-Blinka
# sudo pip3 install adafruit-circuitpython-ssd1306
# sudo apt install python3-pil

import time
import subprocess

import random

import board
import digitalio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306

display_reset = digitalio.DigitalInOut(board.D4)

w = 128
h = 64

white = 255
black = 0

I2C = board.I2C()
d = adafruit_ssd1306.SSD1306_I2C(w, h, I2C, addr=0x3C, reset=display_reset)

d.fill(0)

d.show()


image = Image.new("1", (d.width, d.height))
draw = ImageDraw.Draw(image)

def drawBlackRect():
  draw.rectangle((0, 0, w, h), outline=0, fill=black)

drawBlackRect()

pad = -2
top = pad
bottom = h - pad

x = 0

font = ImageFont.load_default()

count = 0

messages = ["AAA", "BBB", "CCC"]
m_len = len(messages)

while True:
  count = count + 1
  drawBlackRect()
  i = random.randint(0, m_len - 1)
  message = "%s %s" % (messages[i], count)

  draw.text( (x, top), message, font=font, fill=white)

  d.image(image)
  d.show()
  time.sleep(0.5)
  print("loop")