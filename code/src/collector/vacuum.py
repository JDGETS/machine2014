from lib.state import State

class Vacuum(State):

    RUNNING_DURATION = 10
    IDLING_DURATION = 10

    def __init__(self):
        print "Init Vacuum()"

    def start(self):
        self.set_state(self.state_running)

    def state_running(self):
        print "[Vacuum.state_running]"
        yield self.wait(self.RUNNING_DURATION, self.state_idling)

    def state_idling(self):
        print "[Vacuum.state_idling]"
        yield self.wait(self.IDLING_DURATION, self.state_running)

