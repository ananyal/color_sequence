import RPi.GPIO as GPIO
import time
import random
import LEDRGB as LED

colors = ['R', 'G', 'B', 'Y']
R_pin = 11
G_pin = 12
B_pin = 13
LED.setup(R_pin, G_pin, B_pin)

def loop():
    while True:
        n = random.randint(0,3)
        LED.setColor(colors[n])
        time.sleep(0.5)


if __name__ == '__main__':
    try:
        loop()
    except KeyboardInterrupt:
        LED.destroy()
