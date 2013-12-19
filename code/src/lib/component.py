from state import State

class Component(State):
    def __init__(self, init_state):
        self.init_state = init_state

    def start(self):
        self.set_state(self.init_state)

    def stop(self):
        pass