from gpiozero import Buzzer

buzzer = Buzzer(26)

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

def pi():
    beep_pi()

def pi2():
    beep_pi2()
