#! /usr/bin/env python
from camion.camion import Camion
import sys

if __name__ == "__main__":
    c = None
    try:
        print "[main_camion] Start camion."
        c = Camion()
        c.run()
        
    finally:
        if c:
            c.stop()
        print "[main_camion] Stop camion"