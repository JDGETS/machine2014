from servo import Servo
import time

class SortArm(Servo):

    def __init__(self, pin, pull_duty, push_duty):
        Servo.__init__(self, pin, pull_duty)
        self.pull_duty = pull_duty
        self.push_duty = push_duty
        return

    def push(self):
        return self.set(self.push_duty)

    def pull(self):
        return self.set(self.pull_duty)

    def round_trip(self, pause):
        self.push()
        time.sleep(pause)
        self.pull()
        return
