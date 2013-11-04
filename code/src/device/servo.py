import Adafruit_BBIO.PWM as PWM

class Servo:
    DUTY = 1600
    DUTY_CYCLE_PER_ANGLE = 400/45

    def __init__(self, pin):
        self.pin = pin
        PWM.start(self.pin, self.DUTY)

    def set_angle(self, angle):
        duty_cycle = int(self.DUTY_CYCLE_PER_ANGLE * angle)
        PWM.set_duty_cycle(self.pin, duty_cycle)

    def stop(self):
        PWM.stop(self.pin)
        PWM.cleanup()
