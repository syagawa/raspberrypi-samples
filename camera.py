from gpiozero import LED, Button, Buzzer, PWMLED
from time import sleep
from signal import pause
from subprocess import check_call
from picamera import PiCamera
from datetime import datetime
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


B1 = Button(21)
L1 = LED(17)
CAM = PiCamera()

def shot():
    print("shot!")
    L1.on()
    t = datetime.now().isoformat()
    beep_pi()
    CAM.capture("/home/pi/%s.jpg" % timestamp)
    L1.off()

B1.when_pressed = shot

pause()