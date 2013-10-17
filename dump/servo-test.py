""" Code de test pour les servo.

On utilise un board pololu pour controller le servo.


"""

import Adafruit_BBIO.GPIO as GPIO
from time import sleep

 
GPIO.setup("P8_10", GPIO.OUT)

for x in range(0, 400):
	GPIO.output("P8_10", GPIO.HIGH)
	sleep(0.01)
	GPIO.output("P8_10", GPIO.LOW) 
	sleep(0.01)

