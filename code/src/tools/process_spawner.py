from threading import Thread
from device import Switch
from lib import config
from subprocess import Popen, STDOUT
import sys

SWITCH_ID = "spawn_switch"
spawn_switch = Switch(**config.devices[SWITCH_ID])
target = sys.argv[1:]

class StopProcess(Thread):
    def __init__(self, script, switch):
        self.process = script
        self.switch = switch

    def run(self):
        self.switch.wait_pushed();
        print "[script_spawner] Stop", target
        self.process.terminate()

while True:
    spawn_switch.wait_pushed();
    print "[run_collector] Start", target
    p = Popen(target)
    t = StopProcess(p, spawn_switch)
    p.wait()
    print "[run_collector] Process terminated with code", p.returncode
