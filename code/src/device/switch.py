""" Switch class.

"""

import Adafruit_BBIO.GPIO as GPIO

class Switch(object):
	
	def __init__(self, pin):
		""" Create a Switch object that reads input from the given pin. """
		self.pin = pin
		GPIO.setup(pin, GPIO.IN)
		return
	
	def is_pressed(self):
		""" Return True if the switch is pressed. """
		return GPIO.input(self.pin)

	def is_released(self):
		""" Return True if the switch is not pressed. """
		return not GPIO.input(self.pin)

	def wait_pushed(self):
		""" Wait for the switch to be pressed and released (waits for a falling edge followed by a rising edge. """
		GPIO.wait_for_edge(self.pin, GPIO.FALLING)
		GPIO.wait_for_edge(self.pin, GPIO.RISING)
		return

	def wait_pressed(self):
		""" Wait for the switch to be pressed (waits for a falling edge). """
		GPIO.wait_for_edge(self.pin, GPIO.FALLING)
		return
	