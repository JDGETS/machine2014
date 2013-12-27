""" Switch class.

"""

import Adafruit_BBIO.GPIO as GPIO

class Switch(object):

    def __init__(self, pin):
        """ Create a Switch object that reads input from the given pin. """
        self.pin = pin
        self.last_was_pressed = False
        self.last_detected_pressed = False
        GPIO.setup(pin, GPIO.IN, GPIO.PUD_UP)
        self.rising_edge_callbacks = []
        self.falling_edge_callbacks = []
        GPIO.add_event_detect(pin, GPIO.BOTH, self._edge_event, 10)
    
    def bind_raising_edge(self, funct):
        self.rising_edge_callbacks.append(funct)
        
    def bind_falling_edge(self, funct):
        self.falling_edge_callbacks.append(funct)
        
    def _edge_event(self, event = None):
        inputs = {0:0, 1:0}
        for i in xrange(0,50):
            inputs[GPIO.input(self.pin)] += 1
    
        if inputs[1] > 2: #Observations de Mathieu et Mathieu
            for callback in self.rising_edge_callbacks:
                callback()
            self.last_detected_pressed = GPIO.event_detected(self.pin)
        else:
            for callback in self.falling_edge_callbacks:
                callback()

    def is_pressed(self):
        """ Return True if the switch is pressed. """
        return GPIO.input(self.pin)

    def is_released(self):
        """ Return True if the switch is not pressed. """
        return not GPIO.input(self.pin)

    def was_pressed(self):
        last = self.last_was_pressed
        self.last_was_pressed = self.last_detected_pressed
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