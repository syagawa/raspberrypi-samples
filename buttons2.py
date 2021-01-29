from gpiozero import LED, Button, Buzzer, PWMLED
from time import sleep
from signal import pause
import os

leds = [17, 18, 27, 22, 25, 12, 13, 19]
buttons = [21, 16, 20]
buzzer = Buzzer(26)

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

def beep(times, sec):
    for i in range(times):
        buzzer.on()
        sleep(sec)
        buzzer.off()
        sleep(sec)

def beep_pi():
    beep(1, 0.02)

def beep_pi2():
    beep(2, 0.02)


beep_pi()
allLeds(ON)
sleep(1)
allLeds(OFF)
beep_pi2()

B1 = getBtn(0)
L1 = getLed(0)

B2 = getBtn(1)
L2 = getLed(1)

B3 = getBtn(2)
L3 = PWMLED(27)



B1.when_pressed = L1.on
B1.when_released = L1.off

B2.when_pressed = L2.toggle

B3.when_pressed = L3.pulse

L3.value = 0.1

pause()

