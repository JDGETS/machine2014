import time
from lib.io.servo import Servo

class Piston:
    """Piston controller"""

    def __init__(self, id):
        self.id = id
        self.driver = Servo(self.id)

    def push(self):
        # set servo to push position
        pass

    def pull(self):
        # set servo to pull position
        pass

