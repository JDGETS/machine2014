from collector.rail import Rail
from device import Piston, Switch
from lib import config

print "The correct starting state for the collector is: Truck on sort_position. Gate closed."
r = Rail()
gate = Piston(**config.devices["gate_servo"])
while True:
    print "1 : Goto Home"
    print "2 : Goto Waiting for sort position"
    print "3 : Goto Away (Dump)"
    print "4 : Close gate"
    print "5 : Open gate"
    c = int(raw_input("your choice?"))

    if c ==1:
        print "going home"
        r.slide_to_home()
    if c == 2:
        print "going wait"
        r.slide_to_wait_for_sorting_position()
    if c == 3:
        print "going dump"
        r.slide_to_away()
    if c == 4:
        print "closing gate"
        gate.push()
    if c == 5:
        print "opening gate"
        gate.pull()

