#! /usr/bin/env python
from collector.collector import Collector
import sys, os

if __name__ == "__main__":
    c = None
    try:
        print "[main_collector] Start collector"
        c = Collector()
        c.run()

    finally:
        if c:
            c.stop()
        print "[main_collector] Stop collector"