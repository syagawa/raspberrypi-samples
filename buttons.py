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
        led = LED(num)
        return led

def getBtn(n):
    if n == 0:
        print("not exists")
    elif n > 3:
        print("not exists")
    else:
        num = buttons[n]
        btn = Button(num)
        return btn


N = 2
button = getBtn(N)
led = getLed(N)

while True:
    if button.is_pressed:
        print("pressed")
        led.on()
        sleep(0.5)
        led.off()

    sleep(0.05)


