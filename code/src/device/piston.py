from servo import Servo

class Piston(Servo):
    """Piston controller"""

    def __init__(self, pin, pull_duty, standby_duty, push_duty):
        Servo.__init__(self, pin, pull_duty)
        self.pull_duty = pull_duty
        self.standby_duty = standby_duty
        self.push_duty = push_duty

    def standby(self):
        """set servo to standby position"""
        self.set_duty(self.standby_duty)

    def push(self):
        """set servo to push position"""
        self.set_duty(self.push_duty)

    def pull(self):
        """set servo to pull position"""
        self.set_duty(self.pull_duty)
