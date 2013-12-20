from collector import Collector
from threading import Thread
import time
from lib import ex_pdb

collector = Collector()

ON_SWITCH_ID = "collector_on_switch"

collector_switch = Switch(**config.devices[ON_SWITCH_ID])

def wait_for_signal():
    if not collector_switch.is_pressed():
        collector_switch.wait_pressed();

def wait_for_stop():
    wait_for_signal()
    collector.stop()


while True:
    wait_for_signal()
    t = Thread(target = wait_for_stop)
    t.start()
    collector.run()