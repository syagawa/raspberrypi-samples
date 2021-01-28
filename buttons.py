from gpiozero import LED, Button
from time import sleep
import os

leds = [17, 18, 27, 22, 25, 12, 13, 19]
buttons = [21, 16, 20]
OFF = 0
ON = 1

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

def getAllLeds():
    arr = []
    for i in leds:
        led = getLed(i)
        arr.append(led)
    return arr

def allLeds(mode):
    for i in leds:
        ld = getLed(i)
        if mode == OFF:
            ld.off()
        elif mode == ON:
            ld.on()




allLeds(ON)
sleep(1)
allLeds(OFF)


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

except KeyboardInterrupt:
    offAllLeds()