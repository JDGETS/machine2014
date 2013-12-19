from collector import Vacuum
from lib import ex_pdb
import time

ex_pdb.init()

shaker = VacuumShaker()
time.sleep(1.0)

shaker.start()
shaker.on()

while True:
    shaker.update()