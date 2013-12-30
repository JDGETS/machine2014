from sorter import Sorter
from mono_sorter import MonoSorter
from rail import Rail
from vacuum_shaker import VacuumShaker
from lib import config
from collector_controller import CollectorController
import Adafruit_BBIO.PWM as PWM

class Collector(object):
    def __init__(self):
        print "[Collector.__init__]"
        self.vacuum_shaker = VacuumShaker()
        self.sorter = MonoSorter()
        self.rail = Rail()
        self.controller = CollectorController(self)

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

    def stop(self):
        print "[Collector.run] Collector stopped"
        self.is_running = False

        for c in self.components:
            c.stop()

        PWM.cleanup()

    def force_stop(self):
        self.stop()
        sys.exit(0);
