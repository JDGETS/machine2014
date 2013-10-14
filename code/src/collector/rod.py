import time

class Rod:
    def __init__(self):
        print "Init Rod()"
        self.isMoving = False
        self.isPushed = False
        
    def wait(self):
        while self.isMoving:
            time.sleep(0.01)

    def push(self):
        self.isMoving = True
        #Do something...
        self.isMoving = False
        self.isPushed = True

    def goBack(self):
        self.isMoving = True
        #Do something...
        self.isMoving = False
        self.isPushed = False

