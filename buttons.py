from gpiozero import LED, Button
from time import sleep
import os

leds = [17, 18, 27, 22, 25, 12, 13, 19]
buttons = [21, 16, 20]
OFF = 0
ON = 1

def getLed(n):
    if n < 0:
        print("not exists")
    elif n > 7:
        print("not exists")
    else:
        num = leds[n]
        led = LED(num)
        return led

def getBtn(n):
    if n < 0:
        print("not exists")
    elif n > 2:
        print("not exists")
    else:
        num = buttons[n]
        btn = Button(num)
        return btn

def allLeds(mode):
    for i in leds:
        ld = LED(i)
        if mode == OFF:
            ld.off()
        elif mode == ON:
            ld.on()
        sleep(0.1)



allLeds(ON)
sleep(1)
allLeds(OFF)

B1 = getBtn(0)
L1 = getLed(0)

B2 = getBtn(1)
L2 = getLed(1)

B3 = getBtn(2)
L3 = getLed(2)

while True:
    if B1.is_pressed:
        print("pressed")
        L1.on()
        sleep(0.5)
        L1.off()
    elif B2.is_pressed:
        print("pressed")
        L2.on()
        sleep(0.5)
        L2.off()
    elif B3.is_pressed:
        print("pressed")
        L3.on()
        sleep(0.5)
        L3.off()

    sleep(0.05)

