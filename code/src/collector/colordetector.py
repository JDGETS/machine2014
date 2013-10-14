from lib.observable import Observable

class ColorDetector(Observable):
    """ Encapsule tous les sensors de couleurs """
    def __init__(self):
        print "Init ColorDetector()"
        Observable.__init__(self)
        self.sensors = [] #...
        #Partir un thread pour les sensors?
        
    def detect(self):
        event = DetectedBallEvent("WHITE") # Or ORANGE...
        self.notifyAll(event)

class DetectedBallEvent:
    """ Un evenement de balle detectee.
        WHITE
        ORANGE """
    def __init__(self, color):
        self.color = color;
    