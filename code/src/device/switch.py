""" Switch class.

"""

import Adafruit_BBIO.GPIO as GPIO
import time

class Switch(object):

    def __init__(self, pin, detect_edges = None):
        """ Create a Switch object that reads input from the given pin. """
        self.pin = pin
        self.last_detected_pressed_id = 0
        self.current_detected_pressed_id = 0
        GPIO.setup(pin, GPIO.IN, GPIO.PUD_UP)
        self.rising_edge_callbacks = []
        self.falling_edge_callbacks = []
        self.edges_detected = detect_edges
        if detect_edges != None:
            GPIO.add_event_detect(pin, detect_edges, self._edge_event, 50)

    def bind_rising_edge(self, funct):
        self.rising_edge_callbacks.append(funct)

    def bind_falling_edge(self, funct):
        self.falling_edge_callbacks.append(funct)

    def clear_bindings(self):
        self.rising_edge_callbacks = []
        self.falling_edge_callbacks = []

    def _edge_event(self, event = None):
        #Ugly code - c'est la faute de Lavoie
        if self.edges_detected == GPIO.BOTH:
            inputs = {0:0, 1:0}
            for i in xrange(0,100):
                inputs[GPIO.input(self.pin)] += 1
                if i % 10 == 0:
                    time.sleep(0.05)

            if inputs[1] > 2: #Observations de Mathieu et Mathieu
                for callback in self.rising_edge_callbacks:
                    callback()
                self.current_detected_pressed_id += 1
            else:
                for callback in self.falling_edge_callbacks:
                    callback()
        elif self.edges_detected == GPIO.RISING:
            for callback in self.rising_edge_callbacks:
                callback()
            self.current_detected_pressed_id += 1
        elif self.edges_detected == GPIO.FALLING:
            for callback in self.falling_edge_callbacks:
                callback()


    def is_pressed(self):
        """ Return True if the switch is pressed. """
        return GPIO.input(self.pin)

    def is_released(self):
        """ Return True if the switch is not pressed. """
        return not GPIO.input(self.pin)

    def was_pressed(self):
        last = self.last_detected_pressed_id
        self.last_detected_pressed_id = self.current_detected_pressed_id
        return last != self.current_detected_pressed_id

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