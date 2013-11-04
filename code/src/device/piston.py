from lib.io.servo import Servo

class Piston:
    """Piston controller"""

    def __init__(self, pin):
        self.pin = pin
        self.driver = Servo(self.pin)

    def push(self):
        # set servo to push position
        pass

    def pull(self):
        # set servo to pull position
        pass

