from lib.state import State
from device import DigitalOutput, pin_from_id

class Vacuum(State):

    RUNNING_DURATION = 10
    IDLING_DURATION = 10
    VACUUM_ID = "vacuum"

    def __init__(self):
        print "Init Vacuum()"
        self.vacuum_output = DigitalOutput(pin_from_id(self.VACUUM_ID))

    def start(self):
        self.set_state(self.state_running)

    def stop(self):
        self.vacuum_output.off()

    def state_running(self):
        print "[Vacuum.state_running]"
        self.vacuum_output.on()
        yield self.wait(self.RUNNING_DURATION, self.state_idling)

    def state_idling(self):
        print "[Vacuum.state_idling]"
        self.vacuum_output.off()
        yield self.wait(self.IDLING_DURATION, self.state_running)

