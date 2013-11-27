import sys
import time
sys.path.append('../src')

from device import ColorSensor
from lib import ex_pdb, config

ex_pdb.init()

color_sensor = ColorSensor(**config.devices["color_sensor"])

colors = ["Black", "White", "Orange", "Unknown"]

while True:
    print "Color detected: ", colors[color_sensor.get_color()]
