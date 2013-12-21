#! /usr/bin/env python
from camion.camion import Camion
import sys


def mainSafe():
    #try:
    camion = Camion()
    camion.run()

    #except:
    #    print "Exception raised  in maincamion::mainSafe", sys.exc_info()[0]
    #    camion.stop()
    #    raise

if __name__ == "__main__":
    mainSafe();