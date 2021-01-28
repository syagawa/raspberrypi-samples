from gpiozero import LED, Button
from time import sleep
import os

LED1 = LED(17)
LED2 = LED(18)
LED3 = LED(27)
LED4 = LED(22)
LED5 = LED(25)
LED6 = LED(12)
LED7 = LED(13)
LED8 = LED(19)


BTN1 = Button(21)
BTN2 = Button(16)
BTN3 = Button(20)

try:
  while True:
    if BTN1.is_pressed:
      LED1.on()
    sleep(0.05)
