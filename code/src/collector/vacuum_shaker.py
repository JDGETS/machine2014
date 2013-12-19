from lib.component import Component
from device import Piston
from lib import config

class VacuumShaker(Component):

    PULL_DELAY = 1
    PUSH_DELAY = 1

    VACUUM_SERVO_ID = "vacuum_servo"

    def __init__(self):
        super(VacuumShaker, self).__init__(self.state_idling)
        print "[VacuumShaker.__init__]"

        self.vacuum_servo = Piston(**config.devices[self.VACUUM_SERVO_ID])
        self.is_shaking = False

    def on(self):
        self.is_shaking = True

    def off(self):
        self.is_shaking = False

    def stop(self):
        print "[VacuumShaker.stop] Stoping"
        self.vacuum_servo.stop()

    def state_push(self):
        print "[VacuumShaker.state_push]"
        self.vacuum_servo.push()
        if not self.is_shaking:
            yield self.state_idling

        yield self.wait(self.PUSH_DELAY, self.state_pull)

    def state_pull(self):
        print "[VacuumShaker.state_pull]"
        self.vacuum_servo.pull()
        if not self.is_shaking:
            yield self.state_idling

        yield self.wait(self.PULL_DELAY, self.state_push)

    def state_idling(self):
        print "[VacuumShaker.state_idling]"
        self.vacuum_servo.standby()

        while not self.is_shaking:
            yield

        yield self.state_push

