from gpiozero import LED, Button, Buzzer, PWMLED
from time import sleep
from signal import pause
from subprocess import check_call
from picamera import PiCamera
from datetime import datetime
from modules import buttons
import os

CAM = PiCamera()
CAM.resolution = (1920, 1080)

def shot(led):
    print("shot!")
    led.on()
    t = datetime.now().isoformat()
    #beep_pi()
    if os.path.exists("./images") == False:
        os.makedirs("./images")
    CAM.capture("./images/%s.jpg" % t)
    led.off()

def shots(count, interval, led):
    for i in range(count):
        shot(led)
        sleep(interval)

def setShots(count, interval, led):
    n = count
    i = interval
    def f():
        shots(n, i, led)
    return f
