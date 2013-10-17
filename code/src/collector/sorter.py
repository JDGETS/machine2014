import time
from functools import partial

from device import Piston, ColorSensor

class Sorter:
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

        self.piston_pushed = self.white_piston

    def start(self):
        self.state = self.state_push()

    def update(self):
        try:
            state = self.state.next()
            if state != None:
                self.state = state()
        except StopIteration:
            "Sorter's state machine done."


    def state_push(self):
        """State that move one piston to push a ball
        change to 'state_pushed' after a small delay"""

        print "[Sorter.state_push]"

        self.piston_pushed.push()
        start_time = time.clock()
        while(time.clock() - start_time < self.PUSH_DELAY):
            yield

        yield self.state_pushed

    def state_pushed(self):
        """State that wait for a balls. Read ball's color and
        change to 'state_recall' after setting the good piston"""

        print "[Sorter.state_pushed]"

        ball_color = self.color_sensor.get_color()
        while ball_color == ColorSensor.UNKOWN:
            yield
            ball_color = self.color_sensor.get_color()

        current_piston_pushed = self.piston_pushed

        if ball_color == ColorSensor.WHITE:
            print "[Sorter.state_pushed] White ball detected"
            self.piston_pushed = self.white_piston
        else:
            print "[Sorter.state_pushed] Orange ball detected"
            self.piston_pushed = self.orange_piston

        yield partial(self.state_pull, current_piston_pushed)

    # state that move back a piston

    def state_pull(self, piston_to_recall):
        """move back piston_to_recall. Change to 'state_push' after the PULL_DELAY"""

        print "[Sorter.state_pull]"

        piston_to_recall.pull()

        start_time = time.clock()
        while(time.clock() - start_time < self.PULL_DELAY):
            yield

        yield self.state_push

