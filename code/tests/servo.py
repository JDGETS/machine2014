import sys
import time
sys.path.append('../src')

from device import Servo
from lib import ex_pdb

ex_pdb.init()

pull = 13
push = 10.3

servo = Servo("P9_16", pull, push)

servo.push()
time.sleep(2)
servo.pull()

raw_input("Press key...")
servo.stop()
