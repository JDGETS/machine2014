#! /usr/bin/env python
from collector.collector import Collector
import sys, os

def mainSafe():
    c = None
    try:
        print "[main_collector] Start collector"
        c = Collector()
        c.run()

    except Exception as e:
        print "[main_collector] Exception raised in main_collector::mainSafe"
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno)
        raise e
        
    finally:
        if c:
            c.stop()
        print "[main_collector] Stop collector"

if __name__ == "__main__":
    mainSafe();