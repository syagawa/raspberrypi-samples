from gpiozero import LED, Button, Buzzer, PWMLED
from time import sleep
from signal import pause
import os

leds = [17, 18, 27, 22, 25, 12, 13, 19]
buttons = [21, 16, 20]
buzzer = Buzzer(26)

OFF = 0
ON = 1

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


def doexe():
    print("longpress")
    L1.toggle()


B1 = Button(21, hold_time=0.5)
L1 = LED(17)

B1.when_held = doexe

