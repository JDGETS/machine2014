import Adafruit_BBIO.PWM as PWM

class Servo(object):

    def __init__(self, pin, duty):
        self.pin = pin
        self.duty = duty
        PWM.start(self.pin, self.duty, 50, 1)
        print 'started', self.pin
        return

    def set(self, duty):
        self.duty = duty
        PWM.start(self.pin, self.duty, 50, 1)
        PWM.set_duty_cycle(self.pin, self.duty)
        return

    def stop(self):
        #PWM.stop(self.pin)
        return
