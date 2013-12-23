from switch import Switch
import time


class MagneticSwitch(Switch):

    def __init__(self, pin):
        """ Create a Switch object that reads input from the given pin. """
        self.pin = pin
        self.last_was_pressed = False
        GPIO.setup(pin, GPIO.IN, GPIO.PUD_UP)
        GPIO.add_event_detect(pin, GPIO.RISING)
    
    def wait_released(self):
        """ Wait for the switch to be released (waits for a raising edge). YES. This is important with magnetic switches. And wait_released is already blocking so leave me alone with the time.sleep! """
        while not self.is_released():
            time.sleep(0.01)
            
    def wait_pressed(self):
        """ Wait for the switch to be released (waits for a raising edge). YES. This is important with magnetic switches. And wait_released is already blocking so leave me alone with the time.sleep! """
        while not self.is_pressed():
            time.sleep(0.01)

