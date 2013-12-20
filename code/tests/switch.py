from device import Switch
import sys

pin = sys.argv[1]
s = Switch(pin)
s.wait_pushed()
print "Switch pushed"
