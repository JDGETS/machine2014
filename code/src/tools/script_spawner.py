from threading import Thread
from device import Switch
from lib import config
import sys

SWITCH_ID = "spawn_switch"
spawn_switch = Switch(**config.devices[SWITCH_ID])

class StopScript(Thread):
    def __init__(self, script, switch):
        self.script = script
        self.switch = switch

    def run(self):
        self.switch.wait_pushed();
        print "[script_spawner] Stop", self.script
        self.script.stop()

__module = __import__(sys.argv[1])

while True:
    spawn_switch.wait_pushed();
    print "[run_collector] Reload", __module
    reload(__module)
    t = StopScript(__module, spawn_switch)
    print "[run_collector] Start", __module
    __module.start()
