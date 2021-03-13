# sudo apt install python3-pip
# sudo pip3 install Adafruit-Blinka
# sudo pip3 install adafruit-circuitpython-ssd1306
# sudo apt install python3-pil
# for 128 * 64 display

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
rows = 8
columns = 21

white = 255
black = 0

pad = -2
top = pad
bottom = h - pad
line_height = 8
x = 0


I2C = board.I2C()
d = adafruit_ssd1306.SSD1306_I2C(w, h, I2C, addr=0x3C, reset=display_reset)

d.fill(0)
d.show()
image = Image.new("1", (d.width, d.height))
draw = ImageDraw.Draw(image)
font = ImageFont.load_default()


def drawBlackRect():
  draw.rectangle((0, 0, w, h), outline=0, fill=black)

def drawWhiteRect():
  draw.rectangle((0, 0, w, h), outline=0, fill=white)

def displayMessage(mes, line):
  l = line - 1
  draw.text( (x, top + (line_height * l) ), mes, font=font, fill=white)



drawBlackRect()


count = 0

messages = ["AAA", "BBB", "CCC"]
m_len = len(messages)

while True:
  count = count + 1
  drawBlackRect()
  i = random.randint(0, m_len - 1)
  message = "%s %s" % (messages[i], count)

  l = random.randint(1, 8)
  displayMessage(message, l)

  d.image(image)
  d.show()
  time.sleep(0.5)
  print("loop")