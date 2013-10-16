#! /usr/bin/env python
# -*- coding: utf-8 -*- 
"""
    On essait de stimuler les stimulis physiques.
"""
import time
from simulation import SimulatedEnvironnement

if __name__ == "__main__":
    simulation = SimulatedEnvironnement()
    
    time.sleep(2) #Le temps d'appuyer sur le bouton de GO
    simulation.sendStartSignal();
    
    time.sleep(600) #Simulation de x secondes.

    print simulation.nbBallesDumpees, "balles ont étés dumpées en", simulation.nbSeq, "aller-retours"