#! /usr/bin/env python
from collector.collector import Collector
import sys


def mainSafe():
    try:
        collector = Collector()
        collector.run()

    except:
        print "Exception raised  in maincollector::mainSafe", sys.exc_info()[0]
        collector.stop()
        raise

if __name__ == "__main__":
    mainSafe();