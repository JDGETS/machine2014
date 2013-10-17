""" LED access library.

Can be used to turn any led connected to a gpio pin on or off (set the pin high or low).
"""

import Adafruit_BBIO.GPIO as GPIO

class LED(object):
	
	def __init__(self, pin):
		""" Create a LED object that controls the given pin. The LED is turned off by default. """
		
		self.pin = pin
		GPIO.setup(pin, GPIO.OUT)
		self.off()
		return
	
	def on(self):
		""" Turn the LED on """
		GPIO.output(self.pin, GPIO.LOW)
		return
	
	def off(self):
		""" Turn the LED off """
		GPIO.output(self.pin, GPIO.HIGH)
		return
	
	def is_on(self):
		""" Return True if the LED is on """
		return GPIO.input(self.pin)
