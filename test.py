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


beeps.pi_micro()
leds.waveFromLeft()
sleep(1)
leds.waveFromRight()
beeps.pi_micro()


B1 = buttons.getButton(1)
# L1 = leds.getLed(1)
B2 = buttons.getButton(2)
# L2 = leds.getLed(2)
B3 = buttons.getButton(3)
# L3 = leds.getLed(3)

leds.setAllLedsOn()

pause()
