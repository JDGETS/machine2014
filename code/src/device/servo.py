import Adafruit_BBIO.PWM as PWM

class Servo:
    DUTY_MIN = 1120
    DUTY_MAX = 1920
    ANGLE_MAX = 90
    def __init__(self, pin):
        self.pin = pin
        PWM.start(self.pin, self.DUTY_MAX, freq=50)

    def set_angle(self, angle):
        duty = angle/self.ANGLE_MAX. * (self.DUTY_MAX-self.DUTY_MIN) + self.DUTY_MIN
        PWM.set_duty_cycle(self.pin, duty)
        return

    def stop(self):
        PWM.stop(self.pin)
        PWM.cleanup()
