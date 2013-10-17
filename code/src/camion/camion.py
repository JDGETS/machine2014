#! /usr/bin/env python
# -*- coding: utf-8 -*-
import time

from comm import CommCamion
from device import LimitSwitch

class Camion:
    """ Contient la logique du Camion (voir séquence Collector sur Google Drive) """

    COLLECTOR_SWITCH_ID = "foo1"
    DUMP_SWITCH_ID = "foo2"

    def __init__(self):
        print "Init Camion()"
        self.comm = CommCamion()
        self.comm.add_callback(self.receiveComm)
        #Présence camion devant trieuse et devant dump (pour dumper les balles)
        self.switchCollector = LimitSwitch(self.COLLECTOR_SWITCH_ID, self.updateSwitchCollector)
        self.switchDump = LimitSwitch(self.DUMP_SWITCH_ID, self.updateSwitchDump)

    def start(self):
        pass

    def stop(self):
        pass

    def receiveComm(self, event):
        if event.message == "START":
            print "Camion: Starting the collector (pushing the limitswitch)"
            self.startCollector()

    def updateSwitchCollector(self, event):
        if event.activated:
            self.dropWeight()
        else:
            self.retrieveWeight()

    def updateSwitchDump(self, event):
        if event.activated:
            self.dropWeight()
            #wait...
            self.releaseBalls()
            #wait...
            self.retrieveWeight()
        else:
            self.holdBalls()

    def startCollector(self):
        """ Hit the switch on the collector to grab the Camion. """
        pass

    def dropWeight(self):
        """ Lâcher le poid. """
        pass

    def retrieveWeight(self):
        """ Remonter le poids. """
        pass

    def releaseBalls(self):
        """ Relacher les balles dans la zone dump. """
        pass

    def holdBalls(self):
        """ Refermer le container. """
        pass
