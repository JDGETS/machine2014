from servo import Servo

class Piston:
    """Piston controller"""

    def __init__(self, pin, pull_duty, push_duty):
        self.pin = pin
        self.pull_duty = pull_duty
        self.push_duty = push_duty
        self.servo = Servo(self.pin, self.pull_duty)

    def push(self):
        """set servo to push position"""
        self.servo.set_duty(self.push_duty)
        pass

    def pull(self):
        """set servo to pull position"""
        self.servo.set_duty(self.pull_duty)
        pass

    def stop(self):
        self.servo.stop()