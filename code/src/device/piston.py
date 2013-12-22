from servo import Servo

class Piston(object):
    """Piston controller"""

    def __init__(self, pin, pull_duty, standby_duty, push_duty):
        self.pin = pin
        self.pull_duty = pull_duty
        self.standby_duty = standby_duty
        self.push_duty = push_duty
        self.servo = Servo(self.pin, self.pull_duty)

    def standby(self):
        """set servo to standby position"""
        self.servo.set_duty(self.standby_duty)

    def push(self):
        """set servo to push position"""
        self.servo.set_duty(self.push_duty)

    def pull(self):
        """set servo to pull position"""
        self.servo.set_duty(self.pull_duty)

    def stop(self):
        self.servo.stop()