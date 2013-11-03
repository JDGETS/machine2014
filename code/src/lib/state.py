import time

class State:
    def update(self):
        try:
            state = self.state.next()
            if state != None:
                self.state = state()
        except StopIteration:

    def set_state(self, state):
        self.state = state

    def wait(self, delay, next_state):
        start_time = time.clock()
        while(time.clock() - start_time < delay_ms):
            yield

        yield next_state