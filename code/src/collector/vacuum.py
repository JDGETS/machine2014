from lib.component import Component
from device import DigitalOutput
from lib import config

class Vacuum(Component):

    RUNNING_DURATION = 10
    IDLING_DURATION = 10
    VACUUM_ID = "vacuum"

    def __init__(self, vacuum_shaker):
        super(Vacuum, self).__init__(self.state_running)

        print "[Vacuum.__init__]"
        self.vacuum_output = DigitalOutput(config.devices[self.VACUUM_ID]["pin"])
        self.vacuum_shaker = vacuum_shaker

    def stop(self):
        print "[Vacuum.stop] Stop vacuum"
        self.vacuum_output.off()

    def state_running(self):
        print "[Vacuum.state_running]"
        self.vacuum_output.on()
        self.vacuum_shaker.on()

        yield self.wait(self.RUNNING_DURATION, self.state_idling)

    def state_idling(self):
        print "[Vacuum.state_idling]"
        self.vacuum_output.off()
        self.vacuum_shaker.off()
        yield self.wait(self.IDLING_DURATION, self.state_running)

