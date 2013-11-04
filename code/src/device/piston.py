from lib.io.servo import Servo

class Piston:
    """Piston controller"""

    SERVO_PULL_VALUE = 0
    SERVO_PUSH_VALUE = 90

    def __init__(self, pin):
        self.pin = pin
        self.servo = Servo(self.pin)

    def push(self):
        """set servo to push position"""
        self.servo.set_angle(self.SERVO_PUSH_ANGLE)
        pass

    def pull(self):
        """set servo to pull position"""
        self.servo.set_angle(self.SERVO_PULL_ANGLE)
        pass
