import time
from lib.state import State

from functools import partial
from device import Piston, ColorSensor

class Sorter(State):
    """Control the sorting function of the collector.
    Implementation use a simple state machine generator. Each state yield None
    or the next state function. The state machine end when a state return instead
    of yielding

    The states go in this order:
    1. state_push: Push the white piston
    2. state_pushed: Check if there a ball
    3. state_pull: Pull the currently pushed piston
    4. state_push: Push the good piston
    5. Go back to 2.
    """

    PULL_DELAY = 0.3
    PUSH_DELAY = 0.3

    WHITE_PISTON_ID = "foo1"
    ORANGE_PISTON_ID = "foo2"
    COLOR_SENSOR_ID = "foo3"

    def __init__(self):
        self.white_piston = Piston(self.WHITE_PISTON_ID)
        self.orange_piston = Piston(self.ORANGE_PISTON_ID)

        self.color_sensor = ColorSensor(self.COLOR_SENSOR_ID)

        self.active_piston = self.white_piston

    def start(self):
        self.set_state(self.state_push)

    def state_push(self):
        """State that move one piston to push a ball
        change to 'state_pushed' after a small delay"""

        print "[Sorter.state_push]"

        self.active_piston.push()
        yield self.wait(self.PUSH_DELAY, self.state_pushed)

    def state_pushed(self):
        """State that wait for a balls. Read ball's color and
        change to 'state_recall' after setting the good piston"""

        print "[Sorter.state_pushed]"

        ball_color = self.color_sensor.get_color()
        while ball_color == ColorSensor.UNKOWN:
            yield
            ball_color = self.color_sensor.get_color()

        current_piston_pushed = self.active_piston

        if ball_color == ColorSensor.WHITE:
            print "[Sorter.state_pushed] White ball detected"
            self.active_piston = self.white_piston
        else:
            print "[Sorter.state_pushed] Orange ball detected"
            self.active_piston = self.orange_piston

        yield partial(self.state_pull, current_piston_pushed)

    def state_pull(self, piston_to_recall):
        """move back piston_to_recall. Change to 'state_push' after the PULL_DELAY"""

        print "[Sorter.state_pull]"

        piston_to_recall.pull()
        yield self.wait(self.PULL_DELAY, self.state_push)

