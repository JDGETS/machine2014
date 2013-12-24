#! /usr/bin/env python
from camion.camion import Camion
import sys

def mainSafe():
    try:
        print "[main_camion] Start camion"
        c = Camion()
        c.run()

    except:
        print "[main_camion] Exception raised  in main_camion::mainSafe", sys.exc_info()[0]
        raise
        
    finally:
        c.stop()
        print "[main_camion] Stop camion"

if __name__ == "__main__":
    mainSafe();