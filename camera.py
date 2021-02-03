from gpiozero import LED, Button, Buzzer, PWMLED
from time import sleep
from signal import pause
from subprocess import check_call
from picamera import PiCamera
from datetime import datetime
from modules import buttons
import os

leds = [17, 18, 27, 22, 25, 12, 13, 19]
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


#beep_pi()
allLeds(ON)
sleep(1)
allLeds(OFF)


B1 = buttons.getButton(1)
L1 = LED(17)
B2 = buttons.getButton(2)
L2 = LED(18)
B3 = buttons.getButton(3)
L3 = LED(27)

CAM = PiCamera()
CAM.resolution = (1920, 1080)

def shot():
    print("shot!")
    L1.on()
    t = datetime.now().isoformat()
    #beep_pi()
    if os.path.exists("./images") == False:
        os.makedirs("./images")
    CAM.capture("./images/%s.jpg" % t)
    L1.off()

def shots(count, interval):
    for i in range(count):
        shot()
        sleep(interval)

def setShots(count, interval):
    n = count
    i = interval
    def f():
        shots(n, i)
    return f

B1.when_pressed = shot
B2.when_pressed = setShots(10, 0.5)
B3.when_pressed = setShots(1000, 30)


pause()
