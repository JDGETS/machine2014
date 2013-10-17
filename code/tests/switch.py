from device import LimitSwitch
import functools

def onChange(name, state):
    print "[%s] State changed: %d" % (name, state)

name = raw_input("LimitSwitch's GPIO: ")

switch = LimitSwitch(name, functools.partial(onChange, name))
print "LimitSwitch initialized"
while True:
    switch.update()