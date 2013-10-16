#! /usr/bin/env python
# -*- coding: utf-8 -*- 
import time

from vacuum import Vacuum
from sorting import SortingModule
from pieces.switches import LimitSwitch

class Collector:
    """ Contient la logique du Collector (voir séquence Collector sur Google Drive)
    TO-DO: Arrêter le vacuum entre les séquences """
    def __init__(self):
        print "Init Collector()"
        self.vacuum = Vacuum()
        self.sortingModule = SortingModule()
        #Activée au début par le camion
        self.switchCamion = LimitSwitch(self.updateSwitchCamion)
        self.switchCamionReady = LimitSwitch(self.updateSwitchCamionReady) #switch sur le rail pour quand le camion est monté en haut (il faut l'aligner avec la zone tampon du collector)
        #Présence camion devant trieuse et devant dump (pour dumper les balles)
        #TO-DO: On a vraiment besoin d'une switch devant la dump pour la trieuse?!
        #Answer: Oui, pour savoir qu'il faut le ramener x secondes plus tard.
        self.switchCollector = LimitSwitch(self.updateSwitchCollector)
        self.switchDump = LimitSwitch(self.updateSwitchDump)
        #Pour le bouton sur lequel le CO va appuyer apres avoir mis les balles dans l'aquarium
        self.switchAquarium = LimitSwitch(self.updateSwitchAquarium)
        
    def start(self):
        """ Démarrer la trieuse (vacuum et rods) """
        print "Collector: Starting up..."
        self.vacuum.start()
        self.sortingModule.start()
        
    def stop(self):
        """ On l'arrête quand le camion n'est plus attaché après le rail. """
        print "Collector: Stop."
        self.vacuum.stop()
        self.sortingModule.stop()
        #TO-DO: Kill switches ?

    def updateSwitchCamion(self, event):
        if event.activated:
            self.start()
        else:
            pass
            
    def updateSwitchCamionReady(self, event):
        if event.activated:
            self.pushCamionToCollector() #Pour le pousser contre la switch

    def updateSwitchCollector(self, event):
        """ TO-DO: Que faire si le camion arrive avant que l'on ait trié les 20 nouvelles balles ??? """
        if event.activated:
            time.sleep(0.5) #TO-DO: À ajuster... Le temps que le poid du camion touche par terre
            self.releaseBalls()
            time.sleep(1.0) #TO-DO: À ajuster...Le temps que toutes les balles tombent.
            self.pushCamionToDump() 
        else:
            self.holdBalls()
            self.goUp()
            
    def updateSwitchDump(self, event):
        if event.activated:
            time.sleep(1.5) #TO-DO: À ajuster...
            self.pushCamionToCollector() 
                        
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
        print "Collector: releasing "+str(self.sortingModule.countNewBallsTriees)+" balls"
        self.sortingModule.resetNewBallsCount()
        pass
    
    def holdBalls(self):
        """ Refermer la zone tampon. """
        pass

    def pushCamionToDump(self):
        """ Pousser le camion vers le dump. """
        pass
    
    def pushCamionToCollector(self):
        """ Ramener le camion vers le collector. """
        pass