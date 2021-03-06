from lib.component import Component

from functools import partial
from device import Piston, ColorSensor
from lib import config
import time

class Sorter(Component):
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

    PULL_DELAY = 0.15
    PUSH_DELAY = 0.15

    WHITE_PISTON_ID = "white_piston"
    ORANGE_PISTON_ID = "orange_piston"
    COLOR_SENSOR_ID = "color_sensor"
    MAX_BALL = 12
    COLOR_TIMEOUT = 2.0
    BLACK_TIMEOUT = 5.0

    def __init__(self):
        super(Sorter, self).__init__(self.state_push)

        print "[Sorter.__init__]"

        self.white_piston = Piston(**config.devices[self.ORANGE_PISTON_ID]) #C'EST VOULU QUE CA SOIT INVERSE
        self.orange_piston = Piston(**config.devices[self.WHITE_PISTON_ID]) #C'EST VOULU QUE CA SOIT INVERSE

        self.color_sensor = ColorSensor(**config.devices[self.COLOR_SENSOR_ID])

        self.active_piston = self.white_piston

        self.ball_count = 0
        self.white_count = 0
        self.orange_count = 0

        self.last_ball_time = time.time();
        self.cycle_time = time.time();

    def stop(self):
        print "[Sorter.stop] Stop pistons"

        self.white_piston.pull()
        time.sleep(self.PULL_DELAY)
        self.white_piston.stop()

        self.orange_piston.pull()
        time.sleep(self.PULL_DELAY)
        self.orange_piston.stop()

    def reset_ball_count(self):
        self.ball_count = 0
        self.white_count = 0
        self.orange_count = 0
        self.cycle_time = time.time()

    def get_ball_count(self):
        return self.ball_count

    def get_last_ball_time(self):
        return self.last_ball_time

    def get_cycle_time(self):
        return self.cycle_time

    def get_ball_count(self):
        return self.ball_count

    def state_push(self):
        """State that move one piston to push a ball
        change to 'state_pushed' after a small delay"""

        self.active_piston.push()
        yield self.wait(self.PUSH_DELAY, self.state_pushed)

    def state_pushed(self):
        """State that wait for a balls. Read ball's color and
        change to 'state_recall' after setting the good piston"""

        self.active_piston.standby()
        print "[Sorter.state_pushed] Piston in standby, w:%d,o:%d,t:%d" % (self.white_count, self.orange_count, self.ball_count)

        ball_color = self.color_sensor.get_color()
        unknown_timeout = time.time() + self.COLOR_TIMEOUT
        black_timeout = time.time() + self.BLACK_TIMEOUT

        while ball_color in [ColorSensor.UNKNOWN, ColorSensor.BLACK] and \
        time.time() < unknown_timeout and time.time() < black_timeout:
            if ball_color == ColorSensor.BLACK:
                unknown_timeout = time.time() + self.COLOR_TIMEOUT
            yield
            ball_color = self.color_sensor.get_color()

        current_piston_pushed = self.active_piston

        if ball_color == ColorSensor.UNKNOWN:
            print '[Sorter.state_pushed] Unknown ball detected'

        if ball_color == ColorSensor.BLACK:
            print '[Sorter.state_pushed] Sorter.state_pushed timed out'
        elif self.orange_count > self.MAX_BALL or \
        (ball_color == ColorSensor.WHITE and self.white_count <= self.MAX_BALL):
            print "[Sorter.state_pushed] White ball detected"
            self.active_piston = self.white_piston
            self.white_count += 1
            self.ball_count += 1
        else:
            print "[Sorter.state_pushed] Orange ball detected"
            self.active_piston = self.orange_piston
            self.orange_count += 1
            self.ball_count += 1

        self.last_ball_time = time.time();
        yield partial(self.state_pull, current_piston_pushed)

    def state_pull(self, piston_to_recall):
        """move back piston_to_recall. Change to 'state_push' after the PULL_DELAY"""

        piston_to_recall.pull()
        yield self.wait(self.PULL_DELAY, self.state_push)

