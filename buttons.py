from gpiozero import LED, Button
from time import sleep
import os

leds = [17, 18, 27, 22, 25, 12, 13, 19]
buttons = [21, 16, 20]

def getLed(n):
    if n == 0:
        print("not exists")
    elif n > 8:
        print("not exists")
    else:
        num = leds[n]
        LED = LED(num)
        return LED

def getBtn(n):
    if n == 0:
        print("not exists")
    elif n > 3:
        print("not exists")
    else:
        num = buttons[n]
        BTN = Button(num)
        return BTN


N = 3
BTN = getBtn(N)
LED = getLed(N)

while True:
    if BTN.is_pressed:
        print("pressed")
        LED.on()

    sleep(0.05)


