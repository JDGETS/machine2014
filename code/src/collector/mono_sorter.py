from lib.component import Component

from functools import partial
from device import Piston, ColorSensor
from lib import config
import time

class MonoSorter(Component):
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

    PULL_DELAY = 0.25
    PUSH_DELAY = 0.25

    PISTON_ID = "white_piston"
    COLOR_SENSOR_ID = "color_sensor"
    MAX_BALL = 12

    def __init__(self):
        super(Sorter, self).__init__(self.state_push)

        print "[Sorter.__init__]"

        self.piston = Piston(**config.devices[self.PISTON_ID])

        self.color_sensor = ColorSensor(**config.devices[self.COLOR_SENSOR_ID])

        self.ball_count = 0

        self.last_ball_time = time.time();

    def stop(self):
        print "[Sorter.stop] Stop pistons"
        self.piston.stop()

    def reset_ball_count(self):
        self.ball_count = 0

    def get_ball_count(self):
        return self.ball_count

    def get_last_ball_time(self):
        return self.last_ball_time

    def get_ball_count(self):
        return self.ball_count

    def state_push(self):
        """State that move one piston to push a ball
        change to 'state_pushed' after a small delay"""

        print "[Sorter.state_push]"

        self.piston.push()
        yield self.wait(self.PUSH_DELAY, self.state_pushed)

    def state_pushed(self):
        """State that wait for a balls. Read ball's color and
        change to 'state_recall' after setting the good piston"""

        print "[Sorter.state_pushed]"

        self.piston.standby()
        print "[Sorter.state_pushed] Piston in standby"

        ball_color = self.color_sensor.get_color()
        while ball_color == ColorSensor.UNKNOWN or ball_color == ColorSensor.BLACK:
            yield
            ball_color = self.color_sensor.get_color()

        self.ball_count += 1
        self.last_ball_time = time.time();
        yield partial(self.state_pull, self.piston)

    def state_pull(self, piston_to_recall):
        """move back piston_to_recall. Change to 'state_push' after the PULL_DELAY"""

        print "[Sorter.state_pull]"

        piston_to_recall.pull()
        yield self.wait(self.PULL_DELAY, self.state_push)

