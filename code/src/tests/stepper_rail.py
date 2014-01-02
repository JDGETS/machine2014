import lib.config
import atexit
from device.stepper import *

stepper = Stepper(**lib.config.devices["stepper_rail"])
atexit.register(stepper.stop)
while True:
    steps = int(raw_input("steps: "))
    direction = int(raw_input("direction (0 or 1):"))
    stepper.move(direction,steps)
