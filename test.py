from gpiozero import LED, Button, Buzzer, PWMLED
from time import sleep
from signal import pause
from subprocess import check_call
from picamera import PiCamera
from datetime import datetime
from modules import buttons, beeps, leds
import os

OFF = 0
ON = 1


beeps.pi()
leds.allLeds(ON)
sleep(1)
leds.allLeds(OFF)
beeps.beep(1, 0.001)


B1 = buttons.getButton(1)
L1 = leds.getLed(1)
B2 = buttons.getButton(2)
L2 = leds.getLed(2)
B3 = buttons.getButton(3)
L3 = leds.getLed(3)

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
