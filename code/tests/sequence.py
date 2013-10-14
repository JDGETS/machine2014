#! /usr/bin/env python
# -*- coding: utf-8 -*- 
"""
    On essait de stimuler les stimulis physiques.
"""

import time
import random
import threading

from collector.collector import Collector
from camion.camion import Camion

class ThreadAspirerBalles(threading.Thread):
    def __init__(self, nbBalles):
        threading.Thread.__init__(self);
        self.nbBalles = nbBalles
        
    def run(self):
        print "Commence à aspirer "+str(self.nbBalles)+" balles"
        for b in xrange(0,self.nbBalles):
            detector.detect("WHITE" if random.random() > 0.5 else "ORANGE");
            time.sleep(random.random()/5) # Random lag (aspirer)
        print "Fini d'aspirer "+str(self.nbBalles)+" balles"

if __name__ == "__main__":
    nbBallesDumpees = 0;
    nbSeq = 0
    
    #Normalement, c'est deux instances indépendantes, mais pour les tests..
    collector = Collector()
    camion = Camion()
    detector = collector.sortingModule.colorDetector
    
    time.sleep(5) # Temps de prendre la télécommande et appuyer sur GOOOO
    
    camion.comm.recv("START"); #Reçu de la télécommande
    collector.switchCamion.activate(); #La limitswitch sur le collector est physiquement activée
    collector.switchCamion.deactivate(); #et désactivée...
    
    #Aspirer 20 balles 
    #TO-DO: il faudrait en aspirer 19 parfois au cas ou une balle soit pognée dans l'aquarium
    aspirerBallesThread = ThreadAspirerBalles(20); 
    aspirerBallesThread.start();
    print "-- Monter le camion"
    time.sleep(10) # Temps de monter le camion
    
    collector.switchCamionReady.activate() #Activer la switch sur le rail
    for i in xrange(0,5):
        ballesDumpes = collector.sortingModule.countNewBallsTriees
        collector.switchCollector.activate() #Le camion finit par atteindre la switch du collector
        camion.switchCollector.activate() #Le camion finit par atteindre la switch du collector
        
        time.sleep(2); #Le temps de dumper les balles
        
        print "-- Going to dump area"
        time.sleep(5); #Le temps d'aller au dump area
        collector.switchDump.activate() #Le camion finit par atteindre la switch du dump
        camion.switchDump.activate() #Le camion finit par atteindre la switch du dump
        time.sleep(2); #Le temps de dumper les balles
        nbBallesDumpees += ballesDumpes
        
        aspirerBallesThread = ThreadAspirerBalles(ballesDumpes); 
        aspirerBallesThread.start();
        
        print "-- Going back to collector"
        time.sleep(5); #Le temps d'aller au collector
                
        nbSeq += 1

    print nbBallesDumpees, "balles ont étés dumpées en", nbSeq, "aller-retours"