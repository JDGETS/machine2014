import Adafruit_BBIO.PWM as PWM
import sys

pin = sys.argv[1]
try:
    PWM.start(pin,5,50,1)
    value = float(sys.read("Value:"))
    PWM.set_duty_cycle(pin,value)
except:
    print "CLEAN"
    PWM.stop(pin)
    PWM.cleanup()

