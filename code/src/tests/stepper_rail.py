import lib.config
from device.stepper import *

stepper = Stepper(lib.config.devices["stepper_rail"])
while True:
    steps = int(raw_input("steps: "))
    direction = int(raw_input("direction (0 or 1):"))
    stepper.move(steps,direction)