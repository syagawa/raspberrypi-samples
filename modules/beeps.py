from gpiozero import Buzzer
from time import sleep

buzzer = Buzzer(26)

def beep(times, sec):
    for i in range(times):
        buzzer.on()
        sleep(sec)
        buzzer.off()
        sleep(sec)


def pi():
    beep(1, 0.02)

def pi2():
    pi()
    pi()

def pi_small():
    beep(1, 0.01)

def pi_micro():
    beep(1, 0.001)