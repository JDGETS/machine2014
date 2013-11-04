from collector import Vacuum
from lib import ex_pdb

ex_pdb.init()

vacuum = Vacuum()
vacuum.start()
while True:
    vacuum.update()