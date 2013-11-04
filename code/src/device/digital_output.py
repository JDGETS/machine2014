import Adafruit_BBIO.GPIO as GPIO

class DigitalOutput(object):

    def __init__(self, pin):
        self.pin = pin
        GPIO.setup(pin, GPIO.OUT)
        self.off()

    def on(self):
        GPIO.output(self.pin, GPIO.LOW)

    def off(self):
        GPIO.output(self.pin, GPIO.HIGH)

    def is_on(self):
        return GPIO.input(self.pin)
