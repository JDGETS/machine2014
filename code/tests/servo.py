from device import Servo
from lib import ex_pdb

ex_pdb.init()

servo = Servo("P0_0")
servo.set_angle(1500/1950)
raw_input("Press key...")
servo.stop()