import time
from functools import partial

class State(object):
    def update(self):
        try:
            state = self.state.next()
            if state != None:
                self.state = state()
        except StopIteration:
            print '[State.update] state machine done'

    def set_state(self, state):
        self.state = state()

    def wait(self, delay, next_state):
        return partial(self.wait_state, delay, next_state)

    def wait_state(self, delay, next_state):
        start_time = time.clock()
        print "[wait_state] start", start_time
        while(time.clock() - start_time < delay):
            print "[wait_state] ", start_time, time.clock(), delay
            yield

        print "[wait_state] done"
        yield next_state

