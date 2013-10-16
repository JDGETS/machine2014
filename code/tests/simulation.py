#! /usr/bin/env python
# -*- coding: utf-8 -*- 
"""
    On essait de stimuler les stimulis physiques.
"""
import time
import random
import thread
import threading

from collector.collector import Collector
from camion.camion import Camion

class SimulatedEnvironnement:
    def __init__(self):
        self.camion = SimulatedCamion(self)
        self.collector = SimulatedCollector(self)
        self.ballesAquarium = 20 #Start à 20
        self.ballesDansCamion = 0 #Au debut, le camion est vide
        self.nbSeq = 0
        self.nbBallesDumpees = 0
    
    def sendStartSignal(self):
        print "SimulatedEnvironnement: Sending START signal"
        self.camion.comm.recv("START"); #Reçu de la télécommande
    
class ThreadAspirerBalles(threading.Thread):
    def __init__(self, env):
        threading.Thread.__init__(self);
        self.env = env
        
    def run(self):
        detector = self.env.collector.sortingModule.colorDetector
        while True:
            if self.env.ballesAquarium != 0:
                nbBalles = self.env.ballesAquarium
                print "Commence à aspirer "+str(nbBalles)+" balles"
                for b in xrange(0,nbBalles):
                    self.env.ballesAquarium -= 1
                    detector.detect("WHITE" if random.random() > 0.5 else "ORANGE");
                    time.sleep(random.random()/5) # Random lag (aspirer)
                print "Fini d'aspirer "+str(nbBalles)+" balles"
            time.sleep(1)
    
class SimulatedCollector(Collector):
    def __init__(self, env):
        Collector.__init__(self)
        self.env = env
        
    def start(self):
        Collector.start(self)
        #Commencer l'aspiration des balles
        aspirerBallesThread = ThreadAspirerBalles(self.env); 
        aspirerBallesThread.start();
        print "-- Monter le camion"
        time.sleep(10) 
        self.switchCamionReady.activate() #Activer la switch sur le rail quand le camion est monté

    def releaseBalls(self):
        self.env.ballesDansCamion = self.sortingModule.countNewBallsTriees
        Collector.releaseBalls(self); #print inside...

    def pushCamionToDump(self):
        print "Collector::pushCamionToDump()"
        print "-- Going to dump area"
        time.sleep(5); #Le temps d'aller au dump area
        thread.start_new_thread(self.switchDump.activate,()) #Le camion finit par atteindre la switch du dump
        thread.start_new_thread(self.env.camion.switchDump.activate,()) #Le camion finit par atteindre la switch du dump
    
    def pushCamionToCollector(self):
        print "Collector::pushCamionToCollector()"
        print "-- Going to collector area"
        time.sleep(5); #Le temps d'aller au dump area
        thread.start_new_thread(self.switchCollector.activate,()) #Le camion finit par atteindre la switch du collector
        thread.start_new_thread(self.env.camion.switchCollector.activate,()) #Le camion finit par atteindre la switch du collector
        self.env.nbSeq += 1 #On recommence la sequence

    def goDown(self):
        print "Collector::goDown()"

    def goUp(self):
        print "Collector::goUp()"
    
    def holdBalls(self):
        print "Collector::holdBalls()"
    
    
class SimulatedCamion(Camion):
    def __init__(self, env):
        Camion.__init__(self)
        self.env = env
        
    def startCollector(self):
        Camion.startCollector(self)
        thread.start_new_thread(self.env.collector.switchCamion.activate,()); #La limitswitch sur le collector est physiquement activée
        thread.start_new_thread(self.env.collector.switchCamion.deactivate,()); #et désactivée...
        
    def releaseBalls(self):
        print "Camion: dumping "+str(self.env.ballesDansCamion)+" sorted balls"
        Camion.releaseBalls(self)
        
        #Remettre autant de balles dans l'aquarium
        print "Adding "+str(self.env.ballesDansCamion)+" balls to the aquarium."
        self.env.ballesAquarium += self.env.ballesDansCamion
        
        #Augmenter les counters
        self.env.nbBallesDumpees += self.env.ballesDansCamion
        self.env.ballesDansCamion = 0
    
    