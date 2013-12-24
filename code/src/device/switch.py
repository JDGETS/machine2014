""" Switch class.

"""

import Adafruit_BBIO.GPIO as GPIO

class Switch(object):

    def __init__(self, pin):
        """ Create a Switch object that reads input from the given pin. """
        self.pin = pin
        self.last_was_pressed = False
        GPIO.setup(pin, GPIO.IN)
        self.callback_trigger = None
        GPIO.add_event_detect(pin, GPIO.FALLING, self.event_triggered)
    
    def bind_event_detect(self, funct):
        self.callback_trigger = funct
        
    def event_triggered(self, event = None):
        if self.callback_trigger:
            self.callback_trigger()
        self.callback_trigger = None

    def is_pressed(self):
        """ Return True if the switch is pressed. """
        return GPIO.input(self.pin)

    def is_released(self):
        """ Return True if the switch is not pressed. """
        return not GPIO.input(self.pin)

    def was_pressed(self):
        last = self.last_was_pressed
        self.last_was_pressed = GPIO.event_detected(self.pin)
        return self.last_was_pressed and last != self.last_was_pressed

    def wait_pushed(self):
        """ Wait for the switch to be pressed and released (waits for a falling edge followed by a rising edge. """
        GPIO.wait_for_edge(self.pin, GPIO.FALLING)
        GPIO.wait_for_edge(self.pin, GPIO.RISING)
        return

    def wait_pressed(self):
        """ Wait for the switch to be pressed (waits for a falling edge). """
        GPIO.wait_for_edge(self.pin, GPIO.FALLING)
        return
        
    def wait_released(self):
        """ Wait for the switch to be released (waits for a raising edge). """
        GPIO.wait_for_edge(self.pin, GPIO.RISING)
        return