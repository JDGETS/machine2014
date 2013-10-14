

class LimitSwitch:
    def __init__(self, callback = None):
        self.callbacks = []
        if callback:
            self.add_callback(callback)
    
    def activate(self):
        self.notifyAll(SwitchEvent(True))

    def deactivate(self):
        self.notifyAll(SwitchEvent(False))

    def notifyAll(self, event):
        for callback in self.callbacks:
            callback(event)

    def add_callback(self, c):
        self.callbacks.push(c);
        
class SwitchEvent:
    def __init__(self, activated):
        self.activated = activated