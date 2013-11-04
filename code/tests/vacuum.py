from collector import Vacuum
import ex_pdb

ex_pdb.init()

vacuum = Vacuum()
vacuum.start()
while True:
    vacuum.update()