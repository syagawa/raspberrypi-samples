from gpiozero import LED, Button, Buzzer, PWMLED
from time import sleep
from signal import pause
from subprocess import check_call
from picamera import PiCamera
from datetime import datetime
from modules import buttons, beeps, leds, shot, display, screen
import os
import random

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



shot.set(True)
# B1.when_pressed = shot.setShots(500, 30, L1)

# B2.when_pressed = shot.setShots(250, 60, L2)

# B3.when_pressed = shot.setShots(125, 120, L3)


sc1 = screen.makeScreen(4)
sc2 = screen.makeScreen(4)

sc1["add"]("Mode is A")
sc2["add"]("Waiting")
screen.show()

sleep(0.5)

sc1["clear"]()
screen.show()


# print(ind)
# while True:
#     mes1 = str(random.randint(1,1000)) + "bbbb"
#     mes2 = str(random.randint(1,1000)) + "AAAA"
#     addScreen1(mes1)
#     addScreen2(mes2)
#     screen.show()
#     sleep(1)

pause()