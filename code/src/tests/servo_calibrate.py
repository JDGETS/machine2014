import Adafruit_BBIO.PWM as PWM
import sys

pin = sys.argv[1]
try:
    PWM.start(pin,5,50,1)
    value = float(raw_input("Value:"))
    PWM.set_duty_cycle(pin,value)
except Exception e:
    print e
    PWM.stop(pin)
    PWM.cleanup()

