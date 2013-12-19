from collector import Vacuum
from lib import ex_pdb

ex_pdb.init()

shaker = VacuumShaker()
shaker.start()
shaker.on()

while True:
    shaker.update()