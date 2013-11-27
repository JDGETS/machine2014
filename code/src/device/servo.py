import Adafruit_BBIO.PWM as PWM

class Servo(object):

    def __init__(self, pin, init_duty):
        self.pin = pin
        PWM.start(self.pin, init_duty, 50, 1)

    def set_duty(self, duty):
        PWM.set_duty_cycle(self.pin, duty)

    def stop(self):
        PWM.stop(self.pin)
