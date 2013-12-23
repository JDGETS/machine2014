from camion.camion import Camion
from device import Piston, Switch
from lib import config

print "The correct starting state for the truck is: Truck on sort_position. Gate closed."
camion = Camion()
while True:
    print "1 : Goto X up (lift foot)"
    print "2 : Goto X down (drop foot)"
    print "3 : Close gate"
    print "4 : Open gate"
    c = int(raw_input("your choice?"))
  
    if c == 1:
        c = int(raw_input("how much? "))
        camion.foot_stepper.move(camion.LIFT_FOOT_DIRECTION,abs(c))
    elif c == 2:
        c = int(raw_input("how much? "))
        camion.foot_stepper.move(camion.DROP_FOOT_DIRECTION,abs(c))

