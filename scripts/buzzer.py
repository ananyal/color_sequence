import RPi.GPIO as GPIO
import time
import random

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

buzz_pin = 32

GPIO.setup(buzz_pin, GPIO.OUT)
Buzz = GPIO.PWN(buzz_pin, 1000)

frequencies = [220, 440, 880, 1760]
n = random.randint(0,3)
Buzz.ChangeFrequency(frequencies[n])
Buzz.start(50)
time.sleep(0.5)
Buzz.stop()
