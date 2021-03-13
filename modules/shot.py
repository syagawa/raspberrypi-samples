from gpiozero import LED, Button, Buzzer, PWMLED
from time import sleep
from signal import pause
from subprocess import check_call
from picamera import PiCamera
from datetime import datetime
from modules import buttons, display
import os

CAM = PiCamera()

def set(upset):
    CAM.resolution = (1920, 1080)
    if upset:
        CAM.vflip = True
        CAM.hflip = True
    else:
        CAM.vflip = False
        CAM.hflip = False


def shot(led, message):
    mes = 'shot! %s' % message
    print(mes)
    display.showMessage(mes, 1)
    led.on()
    t = datetime.now().isoformat()
    #beep_pi()
    if os.path.exists("./images") == False:
        os.makedirs("./images")
    CAM.capture("./images/%s.jpg" % t)
    led.off()

def shots(count, interval, led):
    seconds = count * interval
    minutes = seconds / 60
    hours = minutes / 60
    print('%s hours' % hours)
    for i in range(count):
        mes = '%s / %s interavl: %s' % (i + 1, count, interval)
        shot(led, mes)
        sleep(interval)

def setShots(count, interval, led):
    n = count
    i = interval
    def f():
        shots(n, i, led)
    return f
