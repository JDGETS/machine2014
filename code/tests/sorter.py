from collector import Sorter
from lib import ex_pdb

ex_pdb.init()

sorter = Sorter()
sorter.start()
while True:
    sorter.update()