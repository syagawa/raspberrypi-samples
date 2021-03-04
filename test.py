from gpiozero import LED, Button, Buzzer, PWMLED
from time import sleep
from signal import pause
from subprocess import check_call
from picamera import PiCamera
from datetime import datetime
from modules import buttons, beeps, leds, shot
import os

OFF = 0
ON = 1

modes_length = 8
modes = []

for i in range(modes_length):
    n = i + 1
    modes.append(n)

mode_max = modes_length - 1
mode_min = 0
mode_index = 0

beeps.pi_micro()
leds.waveFromLeft()
sleep(0.5)
beeps.pi_micro()
leds.waveFromRight()
beeps.pi_micro()


B1 = buttons.getButton(1)
# L1 = leds.getLed(1)
B2 = buttons.getButton(2)
# L2 = leds.getLed(2)
B3 = buttons.getButton(3)
# L3 = leds.getLed(3)

leds.setAllLedsOn()
sleep(0.5)
leds.setAllLedsOff()

def showMode():
    print(mode_index)
    for num in modes:
        led = leds.getLed(num)
        current = modes[mode_index]
        if num == current:
            led.on()
        else:
            led.off()

def blinkMode():
    print(mode_index)
    current = modes[mode_index]
    led = leds.getLed(current)
    led.blink(0.5, 0.1, None, True)

def moveToBlinkMode(sec=0.5):
    sleep(sec)
    blinkMode()

def rightMode():
    global mode_index
    mode_index = mode_index + 1
    if mode_index > mode_max:
        mode_index = 0
    showMode()
    moveToBlinkMode()

def leftMode():
    global mode_index
    mode_index = mode_index - 1
    if mode_index < mode_min:
        mode_index = mode_max
    showMode()
    moveToBlinkMode()

# B1.when_pressed = blinkMode
# B2.when_pressed = leftMode
# B3.when_pressed = rightMode

# blinkMode()

shot.set(True)
L1 = leds.getLed(1)
B1.when_pressed = shot.setShots(500, 15, L1)

L2 = leds.getLed(2)
B2.when_pressed = shot.setShots(500, 30, L2)

L3 = leds.getLed(3)
B3.when_pressed = shot.setShots(500, 60, L3)

pause()
