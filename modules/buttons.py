from gpiozero import LED, Button, Buzzer, PWMLED

buttons = [21, 16, 20]

def getButton(n):
    min = 1
    max = len(buttons) + 1
    num = n + 1
    if num < min:
        print("not exists")
    elif num > max:
        print("not exists")
    else:
        i = buttons[num]
        btn = Button(i)
        return btn
