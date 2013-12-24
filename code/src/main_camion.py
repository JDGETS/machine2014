#! /usr/bin/env python
from camion.camion import Camion
import sys

if __name__ == "__main__":
    c = None
    try:
        print "[main_camion] Start camion"
        c = Camion()
        c.run()

    except Exception as e:
        print "[main_camion] Exception raised in main_camion::mainSafe"
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno)
        raise e
        
    finally:
        if c:
            c.stop()
        print "[main_camion] Stop camion"