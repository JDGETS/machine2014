from lib.component import Component
from device import Piston, Switch
from lib import config
from functools import partial
from vacuum_shaker_piston import VacuumShakerPiston
import time

class VacuumShaker(Component):

    SERVO_DELAY = 0.25
    PULL_UP_DELAY = 0.5
    WAIT_TIMEOUT = 30.0
    SHAKE_COUNT = 4

    VACUUM_SERVO_ID = "vacuum_servo"
    LOAD_TANK_SWITCH = "load_tank_switch"

    def __init__(self):
        super(VacuumShaker, self).__init__(self.state_pull_up)
        print "[VacuumShaker.__init__]"

        self.vacuum_servo = VacuumShakerPiston(**config.devices[self.VACUUM_SERVO_ID])
        self.load_tank_switch = Switch(**config.devices[self.LOAD_TANK_SWITCH])
        self.vacuum_servo.complete_standby()

    def stop(self):
        print "[VacuumShaker.stop] Stoping"
        self.vacuum_servo.stop()

    def state_wait_ball(self):
        print "[VacuumShaker.state_wait_ball]"

        self.vacuum_servo.pull()
        start_time = time.time()

        while not self.load_tank_switch.was_pressed() \
            and time.time() < start_time + self.WAIT_TIMEOUT:
            yield

        yield partial(self.state_push, 0)

    def state_pull_up(self):
        print "[VacuumShaker.state_pull_up]"
        if self.load_tank_switch.was_pressed():
            yield self.state_wait_ball

        self.vacuum_servo.standby()
        yield self.wait(self.PULL_UP_DELAY, partial(self.state_push, 0))

    def state_push(self, n):
        print "[VacuumShaker.state_push]"
        if self.load_tank_switch.was_pressed():
            yield self.state_wait_ball

        self.vacuum_servo.push()

        if n < self.SHAKE_COUNT:
            yield self.wait(self.SERVO_DELAY, partial(self.state_pull, n))
        else:
            yield self.wait(self.SERVO_DELAY, self.state_pull_up)

    def state_pull(self, n):
        print "[VacuumShaker.state_pull]"
        if self.load_tank_switch.was_pressed():
            yield self.state_wait_ball

        self.vacuum_servo.pull()
        yield self.wait(self.SERVO_DELAY, partial(self.state_push, n+1))
