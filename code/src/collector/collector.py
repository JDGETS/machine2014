from vacuum import Vacuum
from sorter import Sorter
from vacuum_shaker import VacuumShaker
from lib.io.switch import Switch
from lib import config

class Collector(object):
    ON_SWITCH_ID = "collector_on_switch"

    def __init__(self):
        print "[Collector.__init__]"
        self.vacuum_shaker = VacuumShaker()
        self.vacuum = Vacuum()
        self.sorter = Sorter()

        self.components = [self.sorter, self.vacuum, self.vacuum_shaker]

        self.onSwitch = Switch(**config.devices[self.ON_SWITCH_ID])

    def wait_for_signal(self):
        if not self.onSwitch.is_pressed():
            self.onSwitch.wait_pressed();

        self.run()

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
