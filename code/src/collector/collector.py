from vacuum import Vacuum
from sorter import Sorter
from vacuum_shaker import VacuumShaker

class Collector(object):
    def __init__(self):
        print "[Collector.__init__]"
        self.vacuum_shaker = VacuumShaker()
        self.vacuum = Vacuum(self.vacuum_shaker)
        self.sorter = Sorter()

        self.components = [self.sorter, self.vacuum, self.vacuum_shaker]

    def run(self):
        print "[Collector.run] Start collector"

        for c in self.components:
            c.start()

        print "[Collector.run] Collector started"

        #try:
        while True:
            for c in self.components:
                c.update()
        #except:
        #    print "[Collector.run] Exception catched, stop collector"
        #    self.stop()

    def stop(self):
        for c in self.components:
            c.stop()
