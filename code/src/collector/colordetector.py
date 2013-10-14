

class ColorDetector:
    """ Encapsule tous les sensors de couleurs """
    def __init__(self):
        print "Init ColorDetector()"
        self.callbacks = []
        self.sensors = [] #...
        #Partir un thread pour les sensors?
        
    def detect(self):
        event = DetectedBallEvent("WHITE") # Or ORANGE...
        self.notifyAll(event)
        
    def notifyAll(self, event):
        for callback in self.callbacks:
            callback(event)

    def add_callback(self, c):
        self.callbacks.push(c);

class DetectedBallEvent:
    """ Un evenement de balle detectee.
        WHITE
        ORANGE """
    def __init__(self, color):
        self.color = color;
    