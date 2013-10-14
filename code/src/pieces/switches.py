from lib.observable import Observable

class LimitSwitch(Observable):
    def __init__(self, callback = None):
        Observable.__init__(self, callback)
    
    def activate(self):
        self.notifyAll(SwitchEvent(True))

    def deactivate(self):
        self.notifyAll(SwitchEvent(False))
        
class SwitchEvent:
    def __init__(self, activated):
        self.activated = activated