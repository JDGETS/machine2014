import Adafruit_BBIO.GPIO as GPIO

class DigitalOutput:

    def __init__(self, pin):
        self.pin = pin
        GPIO.setup(self.pin, GPIO.OUT)
        self.off()

    def on(self):
        GPIO.output(self.pin, GPIO.LOW)

    def off(self):
        GPIO.output(self.pin, GPIO.HIGH)

    def is_on(self):
        return GPIO.input(self.pin)
