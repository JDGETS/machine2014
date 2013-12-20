from collector import Collector
from threading import Thread
from device import Switch
import time
from lib import ex_pdb, config

collector = Collector()

ON_SWITCH_ID = "collector_switch"

collector_switch = Switch(**config.devices[ON_SWITCH_ID])

def wait_for_signal():
    if not collector_switch.is_pressed():
        collector_switch.wait_pressed();

def wait_for_stop():
    wait_for_signal()
    print "[run_collector] Stop collector"
    collector.stop()


while True:
    wait_for_signal()
    print "[run_collector] Start collector"
    t = Thread(target = wait_for_stop)
    t.start()
    collector.run()