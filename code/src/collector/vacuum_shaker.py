from lib.component import Component
from device import Piston, Switch
from lib import config
from functools import partial
from vacuum_shaker_piston import VacuumShakerPiston
import time
from lib.logger import Logger

class VacuumShaker(Component):

    SERVO_DELAY = 0.25
    PULL_UP_DELAY = 0.15
    WAIT_TIMEOUT = 2.0 #IN production: 30s (specs)
    SHAKE_COUNT = 4

    VACUUM_SERVO_ID = "vacuum_servo"
    LOAD_TANK_SWITCH = "load_tank_switch"

    SWITCH_TIMEOUT = 1

    def __init__(self):
        super(VacuumShaker, self).__init__(self.state_pull_up)
        print "[VacuumShaker.__init__]"

        self.vacuum_servo = VacuumShakerPiston(**config.devices[self.VACUUM_SERVO_ID])
        self.load_tank_switch = Switch(**config.devices[self.LOAD_TANK_SWITCH], detect_edges=GPIO.RISING)
        self.vacuum_servo.complete_standby()

        self.last_button_push = time.time()

    def stop(self):
        print "[VacuumShaker.stop] Stoping"
        self.vacuum_servo.stop()

    def wait_balls(self):
        self.set_state(self.state_wait_ball);

    def state_wait_ball(self):
        print "[VacuumShaker.state_wait_ball]"

        self.vacuum_servo.complete_standby()
        start_time = time.time()

        while not self.load_tank_switch.was_pressed() \
            and time.time() < start_time + self.WAIT_TIMEOUT:
            yield

        self.last_button_push = time.time()

        Logger().start_new_cycle()

        print "[VacuumShaker.state_push]"
        yield partial(self.state_push, 0)

    def state_pull_up(self):
        if self.load_tank_switch.was_pressed() and time.time() > self.last_button_push + self.SWITCH_TIMEOUT:
            yield self.state_wait_ball

        self.vacuum_servo.standby()
        yield self.wait(self.PULL_UP_DELAY, partial(self.state_push, 0))

    def state_push(self, n):
        if self.load_tank_switch.was_pressed() and time.time() > self.last_button_push + self.SWITCH_TIMEOUT:
            yield self.state_wait_ball

        self.vacuum_servo.push()

        if n < self.SHAKE_COUNT:
            yield self.wait(self.SERVO_DELAY, partial(self.state_pull, n))
        else:
            yield self.wait(self.SERVO_DELAY, self.state_pull_up)

    def state_pull(self, n):
        if self.load_tank_switch.was_pressed() and time.time() > self.last_button_push + self.SWITCH_TIMEOUT:
            yield self.state_wait_ball

        self.vacuum_servo.pull()
        yield self.wait(self.SERVO_DELAY, partial(self.state_push, n+1))
