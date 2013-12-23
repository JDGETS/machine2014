""" Switch class.

"""

import Adafruit_BBIO.GPIO as GPIO

class Switch(object):

    def __init__(self, pin):
        """ Create a Switch object that reads input from the given pin. """
        self.pin = pin
        self.last_was_pressed = False
        GPIO.setup(pin, GPIO.IN)
        self.do_once = None
        GPIO.add_event_detect(pin, GPIO.RISING, self.do_something)

    def do_something(self, event = None):
        if self.do_once:
            self.do_once()
        self.do_once = None
        return

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

import time
class MagneticSwitch(Switch):

    def __init__(self, pin):
        """ Create a Switch object that reads input from the given pin. """
        self.pin = pin
        self.last_was_pressed = False
        GPIO.setup(pin, GPIO.IN, GPIO.PUD_UP)
        self.do_once = None
        GPIO.add_event_detect(pin, GPIO.RISING, self.do_something)
    
    def wait_released(self):
        print "wait_released"
        """ Wait for the switch to be released (waits for a raising edge). YES. This is important with magnetic switches. And wait_released is already blocking so leave me alone with the time.sleep! """
        while not self.is_released():
            time.sleep(0.01)
            
    def wait_pressed(self):
        print "wait_pressed"
        """ Wait for the switch to be released (waits for a raising edge). YES. This is important with magnetic switches. And wait_released is already blocking so leave me alone with the time.sleep! """
        while not self.is_pressed():
            time.sleep(0.01)