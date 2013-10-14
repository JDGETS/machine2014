#! /usr/bin/env python
# -*- coding: utf-8 -*- 
import time
from lib.observable import Observable

class CommCamion(Observable):
    def __init__(self):
        print "Init CommCamion()"
        Observable.__init__(self)

    def recv(self, msg):
        event = CommunicationEvent(msg)
        self.notifyAll(event)

class CommunicationEvent:
    """ Un évènement de communication. """
    def __init__(self, message):
        self.message = message;
