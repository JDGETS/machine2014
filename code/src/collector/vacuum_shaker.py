from lib.component import Component
from device import Piston
from lib import config

class VacuumShaker(Component):

    PULL_DELAY = 0.5
    PUSH_DELAY = 0.5

    VACUUM_SERVO_ID = "vacuum_servo"

    def __init__(self):
        super(VacuumShaker, self).__init__(self.state_push)
        print "[VacuumShaker.__init__]"

        self.vacuum_servo = Piston(**config.devices[self.VACUUM_SERVO_ID])
        self.vacuum_servo.pull()

    def stop(self):
        print "[VacuumShaker.stop] Stoping"
        self.vacuum_servo.stop()

    def state_push(self):
        print "[VacuumShaker.state_push]"
        self.vacuum_servo.push()
        yield self.wait(self.PUSH_DELAY, self.state_pull)

    def state_pull(self):
        print "[VacuumShaker.state_pull]"
        self.vacuum_servo.standby()
        yield self.wait(self.PULL_DELAY, self.state_push)
