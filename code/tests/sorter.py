from collector import Sorter
import ex_pdb

ex_pdb.init()

sorter = Sorter()
sorter.start()
while True:
    sorter.update()