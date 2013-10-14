
class Observable:
    def __init__(self, callback = None):
        self.callbacks = []
        if callback:
            self.add_callback(callback)
    
    def notifyAll(self, event):
        for callback in self.callbacks:
            callback(event)

    def add_callback(self, c):
        self.callbacks.append(c);