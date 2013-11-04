from vacuum import Vacuum
from sorter import Sorter

class Collector:
    def __init__(self):
        print "Init Collector()"
        self.vacuum = Vacuum()
        self.sorter = Sorter()

        self.components = [self.sorter, self.vacuum]

    def run(self):
        self.sorter.start()
        self.vacuum.start()

        for c in self.components:
            c.start()

        while True:
            for c in self.components:
                c.update()
