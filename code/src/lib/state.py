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
        start_time = time.time()
        while(time.time() - start_time < delay):
            yield

        yield next_state

