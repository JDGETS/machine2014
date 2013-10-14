#! /usr/bin/env python
# -*- coding: utf-8 -*- 
import time

from rod import Rod

from lib.observable import Observable

class SortingModule(Observable):
    """ Le module de tri (soit les 2 rods et les sensors de couleur) """
    def __init__(self):
        print "Init SortingModule()"
        Observable.__init__(self)
        self.sensors = [] #...
        #Partir un thread pour les sensors?
        self.countBallsTriees = 0
        self.countNewBallsTriees = 0
        # Il faut les mapper � chaque Rod physique, channel#, ou w.e...
        self.whiteRod, self.orangeRod = Rod(), Rod()
        self.colorDetector = ColorDetector()
        self.colorDetector.add_callback(self.sortBall)
        
    def start(self):
        print "SortingModule::start()"
        #Position de base = 1 rod poussé pour tenir la premiere balle devant les sensors
        self.reinitRods()
        self.whiteRod.push()
          
    def stop(self):
        print "SortingModule::stop()"
        self.reinitRods()
        #TO-DO: Kill switches ?

    def sortBall(self, event):
        self.countBallsTriees += 1
        self.countNewBallsTriees += 1
        #print "Sorting ball #"+str(self.countBallsTriees)+" (color:"+event.color+")"
        self.reinitRods()
        time.sleep(0.3) # Wait for the ball to fall. TO-DO: � OPTIMISER
        if event.color == "WHITE":
            self.whiteRod.push()
        elif event.color == "ORANGE":
            self.orangeRod.push()
        else:
            print "Invalid color in Collector::trier"

    def reinitRods(self):
        for rod in (self.whiteRod, self.orangeRod):
            if rod.isPushed:
                rod.goBack()
                rod.wait()
        
    def resetNewBallsCount(self):
        self.countNewBallsTriees = 0

class ColorDetector(Observable):
    """ Encapsule tous les sensors de couleurs (s'il y en a plus d'un ??) """
    def __init__(self):
        print "Init ColorDetector()"
        Observable.__init__(self)
        self.sensors = [] #...
        #Partir un thread pour les sensors?
        
    def detect(self, color):
        event = DetectedBallEvent(color) # "WHITE" or "ORANGE"...
        self.notifyAll(event)

class DetectedBallEvent:
    """ Un evenement de balle detectee.
        WHITE
        ORANGE """
    def __init__(self, color):
        self.color = color;
    