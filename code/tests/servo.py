import sys
import time
from device import Servo
from lib import ex_pdb

ex_pdb.init()

pin = sys.argv[1]
init_duty = float(sys.argv[2])

servo = Servo(pin, init_duty)

while True:
    c = float(raw_input("Duty? "))
    servo.set_duty(c)

servo.stop()
