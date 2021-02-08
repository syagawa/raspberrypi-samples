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

def allLeds(mode):
    for i in _leds:
        ld = LED(i)
        if mode == OFF:
            ld.off()
        elif mode == ON:
            ld.on()
        sleep(0.1)
