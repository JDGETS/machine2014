from collector.rail import Rail
from device import Piston, Switch
from lib import config

print "The correct starting state for the collector is: Truck on sort_position. Gate closed."
r = Rail()
gate = Piston(**config.devices["gate_servo"])
while True:
    print "TOTAL DISTANCE: "+str(r.HOME_POSITION)
    print "SORTING POSITION: "+str(r.WAIT_FOR_SORTING_POSITION)+" or "+str(r.HOME_POSITION - r.WAIT_FOR_SORTING_POSITION)
    print "1 : Goto X right"
    print "2 : Goto X left"
    print "3 : Close gate"
    print "4 : Open gate"
    c = int(raw_input("your choice?"))
  
    if c == 1:
        c = int(raw_input("how much? "))
        r.stepper.move(0,abs(c))
    elif c == 2:
        c = int(raw_input("how much? "))
        r.stepper.move(1,abs(c))
    elif c == 3:
        print "closing gate"
        gate.push()
    elif c == 4:
        print "opening gate"
        gate.pull()

