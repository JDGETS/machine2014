from threading import Thread
from device import Switch
from lib import config
from subprocess import Popen, STDOUT
import sys
import atexit

pin = sys.argv[1]
target = sys.argv[2:]
spawn_switch = Switch(pin=pin)

class StopProcess(Thread):
    def __init__(self, script, switch):
        Thread.__init__(self)
        self.process = script
        self.switch = switch

    def run(self):
        print "[process_spawner] Wait for switch being pushed to stop process"
        self.switch.wait_pushed();
        print "[process_spawner] Stop", target
        self.process.terminate()

p = None
atexit.register(lambda:p.terminate())

while True:
    print "[process_spawner] Wait for switch being pushed to start process"
    spawn_switch.wait_pushed();
    print "[process_spawner] Start", target
    p = Popen(target)
    t = StopProcess(p, spawn_switch)
    t.start()
    p.wait()
    print "[process_spawner] Process terminated with code", p.returncode
