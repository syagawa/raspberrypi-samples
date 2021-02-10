from gpiozero import LED, Button, Buzzer, PWMLED
from time import sleep

_leds = [17, 18, 27, 22, 25, 12, 13, 19]

OFF = 0
ON = 1

def getLed(n):
    _n = n - 1
    if _n < 0:
        print("not exists")
    elif _n > 7:
        print("not exists")
    else:
        num = _leds[_n]
        led = LED(num)
        return led

def allFromLeft():
    a = []
    for i in _leds:
        ld = LED(i)
        a.append(ld)
    return a

def allFromRight():
    a = []
    for i in (reversed(_leds)):
        ld = LED(i)
        a.append(ld)
    return a

def all():
    return allFromLeft()



def setOn(arr):
    for ld in arr:
        ld.on()

def setOff(arr):
    for ld in arr:
        ld.off()

def setAllLedsOn():
    arr = all()
    setOn(arr)


def waveFromLeft():
    arr = allFromLeft()
    for ld in arr:
        ld.on()
        sleep(0.1)

def waveFromRight():
    arr = allFromRight()
    for ld in arr:
        ld.on()
        sleep(0.1)

def allLeds(mode):
    for i in _leds:
        ld = LED(i)
        if mode == OFF:
            ld.off()
        elif mode == ON:
            ld.on()
        sleep(0.1)
