# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.OUT)

for i in range(5):
    GPIO.output(2, True)
    sleep(2)
    GPIO.output(2, False)
    sleep(2)

GPIO.cleanup()
