#! /usr/bin/env python
from collector.collector import Collector
import sys, os
import time

if __name__ == "__main__":
    c = None
    is_running = True

    while is_running:
        try:
            print "[main_collector] Start collector"
            c = Collector()
            c.run()
            is_running = False
        except Exception as ex:
            "[main_collector] Exception catched:", ex
            time.sleep(10)
        finally:
            if c:
                c.stop()
            print "[main_collector] Stop collector"