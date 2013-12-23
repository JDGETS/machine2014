#! /usr/bin/env python
from collector.collector import Collector
import sys

def mainSafe():
    try:
        print "[main_collector] Start collector"
        collector = Collector()
        collector.run()

    except:
        print "[main_collector] Exception raised in main_collector::mainSafe", sys.exc_info()[0
        raise
        
    finally:
        collector.stop()
        print "[main_collector] Stop collector"

if __name__ == "__main__":
    mainSafe();