from gpiozero import LED, Button, Buzzer, PWMLED

_buttons = [21, 16, 20]

def getButton(n):
    min = 0
    max = len(_buttons)
    num = n - 1
    if num < min:
        print("not exists")
    elif num > max:
        print("not exists")
    else:
        i = _buttons[num]
        btn = Button(i)
        return btn
