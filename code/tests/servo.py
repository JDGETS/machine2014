import sys
import time
sys.path.append('../src')

from device.sort_arm import SortArm
from lib import ex_pdb

ex_pdb.init()

pull = 13
push = 10.3

servo1 = SortArm("P8_19", pull, push)
servo2 = SortArm("P8_13", pull, push)

servo1.round_trip(0.5)
time.sleep(0.5)
servo2.round_trip(0.5)

time.sleep(2)

raw_input("Press key...")
servo2.stop()
servo1.stop()



