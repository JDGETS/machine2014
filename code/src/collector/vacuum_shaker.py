from lib.component import Component
from device import Piston
from lib import config
from functools import partial

class VacuumShaker(Component):

    SERVO_DELAY = 0.25
    PULL_UP_DELAY = 0.5
    SHAKE_COUNT = 4

    VACUUM_SERVO_ID = "vacuum_servo"

    def __init__(self):
        super(VacuumShaker, self).__init__(self.state_pull_up)
        print "[VacuumShaker.__init__]"

        self.vacuum_servo = Piston(**config.devices[self.VACUUM_SERVO_ID])
        self.vacuum_servo.pull()

    def stop(self):
        print "[VacuumShaker.stop] Stoping"
        self.vacuum_servo.stop()

    def state_pull_up(self):
        print "[VacuumShaker.state_pull_up]"
        self.vacuum_servo.pull()
        yield self.wait(self.PULL_UP_DELAY, partial(self.state_push, 0))

    def state_push(self, n):
        print "[VacuumShaker.state_push]"
        self.vacuum_servo.push()

        if n < self.SHAKE_COUNT:
            yield self.wait(self.SERVO_DELAY, partial(self.state_pull, n))
        else:
            yield self.wait(self.SERVO_DELAY, self.state_pull_up)

    def state_pull(self, n):
        print "[VacuumShaker.state_pull]"
        self.vacuum_servo.standby()
        yield self.wait(self.SERVO_DELAY, partial(self.state_push, n+1))
