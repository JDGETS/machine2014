from sorter import Sorter
from rail import rail
from vacuum_shaker import VacuumShaker
from lib import config
from collector_controller import CollectorController

class Collector(object):
    def __init__(self):
        print "[Collector.__init__]"
        self.vacuum_shaker = VacuumShaker()
        self.sorter = Sorter()
        self.rail = Rail()
        self.controller = CollectorController(self.sorter, self.rail)

        self.components = [self.sorter, self.vacuum_shaker, self.rail, self.controller]
        self.is_running = False

    def run(self):
        print "[Collector.run] Start collector"

        for c in self.components:
            c.start()

        print "[Collector.run] Collector started"

        self.is_running = True
        while self.is_running:
            for c in self.components:
                c.update()

        print "[Collector.run] Collector stopped"

        for c in self.components:
            c.stop()

    def stop(self):
        self.is_running = False
