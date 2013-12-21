from lib.component import Component
from device import Piston, Servo, Switch
from sorter import Sorter
from vacuum_shaker import VacuumShaker
from lib import config

class CollectorController(Component):
    
    WAIT_TIME_GATE = 1.0
    WAIT_TIME_FOOT = 2.0
    START_COLLECT = 'start_collect_switch'
    GATE = 'gate_servo'

    def __init__(self, sorter, rail):
        super(CollectorController, self).__init__(self.state_wait_init)
        print "[CollectorController.__init__]"
        self.sorter = sorter
        self.rail = rail
        self.start_collect_switch = Switch(**config.devices[self.START_COLLECT])
        #self.gate = Piston(**config.devices[self.GATE])

    def state_wait_init(self):
        print "[CollectorController.state_wait_init]"

        #Wait for start switch from truck
        if not self.start_collect_switch.is_pressed():
            self.start_collect_switch.wait_pressed()

        yield partial(self.state_push_truck_home, 0)
        
    def state_push_truck_home(self):
        self.rail.slide_to_home()
        
        while not self.rail.is_home():
            yield

        yield partial(self.state_wait_sorter, 0)

    def state_push_truck_away(self):
        self.rail.slide_to_away()
        
        while not self.rail.is_away():
            yield

        yield partial(self.state_push_truck_home, 0)

    def state_push_truck_standby(self):
        self.rail.slide_to_wait_for_sorting_position()

        yield partial(self.state_wait_truck_foot, 0)

    def state_wait_sorter(self):
        print "[CollectorController.state_wait_sorter]"

        #Strategy 1: Don't wait.
        #balls = self.sorter.get_ball_count()
        #while balls < 20 and :
        #    yield

        yield partial(self.state_open_gate, 0)
        
    def state_open_gate(self):
        print "[CollectorController.state_open_gate]"

        #self.gate.XYZ()

        yield self.wait( self.WAIT_TIME_GATE, partial(self.state_close_gate, 0))
        
    def state_close_gate(self):
        print "[CollectorController.state_close_gate]"

        #self.gate.XYZ()

        yield partial(self.state_push_truck_standby, 0)
    
    def state_wait_truck_foot(self):
        yield self.wait( self.WAIT_TIME_FOOT, partial(self.state_push_truck_away, 0))