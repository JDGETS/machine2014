#! /usr/bin/env python
# -*- coding: utf-8 -*- 
import time

from vacuum import Vacuum
from rod import Rod
from colordetector import ColorDetector
from pieces.switches import LimitSwitch

class Collector:
    """ Contient la logique du Collector (voir séquence Collector sur Google Drive)
    TO-DO: Arrêter le vacuum entre les séquences """
    def __init__(self):
        print "Init Collector()"
        self.vacuum = Vacuum()
        self.countBallsTriees = 0
        # Il faut les mapper � chaque Rod physique, channel#, ou w.e...
        self.whiteRod, self.orangeRod = Rod(), Rod()
        self.colorDetector = ColorDetector()
        self.colorDetector.add_callback(self.sortBall)
        #Activée au début quand le camion arrive en haut
        self.switchCamion = LimitSwitch(self.updateSwitchCamion)
        #Présence camion devant trieuse et devant dump (pour dumper les balles)
        #TO-DO: On a vraiment besoin d'une switch devant la dump pour la trieuse?!
        self.switchCollector = LimitSwitch(self.updateSwitchCollector)
        self.switchDump = LimitSwitch(self.updateSwitchDump)
        #Pour le bouton sur lequel le CO va appuyer apres avoir mis les balles dans l'aquarium
        self.switchAquarium = LimitSwitch(self.updateSwitchAquarium)
        
    def start(self):
        """ Declenché quand la limit switch sur la plaque mobile est activee
         par le camion qui arrive en haut. """
        self.vacuum.start()
        #Position de base = 1 rod pouss�e pour tenir la premiere balle devant les sensors
        self.reinitRods()
        self.whiteRod.push()
        
    def stop(self):
        """ On l'arrête quand le camion n'est plus attaché après le rail. """
        self.vacuum.stop()
        self.reinitRods()
        #TO-DO: Kill switches ?

    def sortBall(self, event):
        self.countBallsTriees += 1
        print "Sorting ball #"+str(self.countBallsTriees)+" (color:"+event.color+")"
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

    def updateSwitchCamion(self, event):
        if event.activated:
            self.start()
        else:
            self.stop()

    def updateSwitchCollector(self, event):
        if event.activated:
            self.releaseBalls()
        else:
            self.holdBalls()
            self.goUp()
            
    def updateSwitchDump(self, event):
        pass
                        
    def updateSwitchAquarium(self, event):
        if event.activated:
            self.goDown()
        else:
            pass
        
    def goDown(self):
        """ Descendre la trieuse au niveau de l'eau. """
        pass

    def goUp(self):
        """ Monter la trieuse 2po au dessus de l'eau. """
        pass

    def releaseBalls(self):
        """ Relacher les balles dans la zone tampon. """
        pass
    
    def holdBalls(self):
        """ Refermer la zone tampon. """
        pass
