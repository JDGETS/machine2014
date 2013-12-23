from lib.component import Component
from device import Piston, Switch
from sorter import Sorter
from vacuum_shaker import VacuumShaker
from lib import config
import time

class CollectorController(Component):
    
    WAIT_TIME_GATE = 1.0
    WAIT_TIME_FOOT = 2.0
    WAIT_TIME_DUMP_BALLS = 1.5
    MAX_BALLS_PER_ROUND = 20
    MAX_DELAY_BETWEEN_BALLS = 2.0
    START_COLLECT = 'start_collect_switch'
    GATE = 'gate_servo'
    FOOT_UP = 'collector_foot_up'
    FOOT_DOWN = 'collector_foot_down'

    def __init__(self, sorter, rail):
        super(CollectorController, self).__init__(self.state_wait_init)
        print "[CollectorController.__init__]"
        self.sorter = sorter
        self.rail = rail
        self.start_collect_switch = Switch(**config.devices[self.START_COLLECT])
        self.foot_up_switch = MagneticSwitch(**config.devices[self.FOOT_UP])
        self.foot_down_switch = MagneticSwitch(**config.devices[self.FOOT_DOWN])
        self.gate = Piston(**config.devices[self.GATE])

    def state_wait_init(self):
        print "[CollectorController.state_wait_init]"

        #Wait for start switch from truck
        if not self.start_collect_switch.is_pressed():
            self.start_collect_switch.wait_pressed()

        self.gate.push();
        
        yield self.state_push_truck_home
        
    def state_push_truck_home(self):
        print "[CollectorController.state_push_truck_home]"
        self.rail.slide_to_home()
        
        while self.rail.is_moving():
            yield

        yield self.state_wait_sorter

    def state_push_truck_away(self):
        print "[CollectorController.state_push_truck_away]"
        self.rail.slide_to_away()
        
        while self.rail.is_moving():
            yield

        yield self.wait( self.WAIT_TIME_DUMP_BALLS, self.state_push_truck_home)

    def state_push_truck_standby(self):
        print "[CollectorController.state_push_truck_standby]"
        self.rail.slide_to_wait_for_sorting_position()

        while self.rail.is_moving():
            yield

        yield self.state_wait_truck_foot

    def ready_to_drop_balls(self):
        balls = self.sorter.get_ball_count()
        last_ball_time = self.sorter.get_last_ball_time()
        
        done = balls >= self.MAX_BALLS_PER_ROUND
        halfway_done = balls >= self.MAX_BALLS_PER_ROUND/2
        timed_out = int(time.time() - last_ball_time) > self.MAX_DELAY_BETWEEN_BALLS
        
        return done or (halfway_done and timed_out)
        
    def state_wait_sorter(self):
        print "[CollectorController.state_wait_sorter]"

        while not self.ready_to_drop_balls():
            yield
        
        if self.sorter.get_ball_count() < self.MAX_BALLS_PER_ROUND:
            print "[CollectorController.state_wait_sorter] Timed out. Dumping "+str(self.sorter.get_ball_count())+" balls!"
            
        self.sorter.reset_ball_count()

        yield self.state_open_gate
        
    def state_open_gate(self):
        print "[CollectorController.state_open_gate]"

        self.gate.pull()

        yield self.wait( self.WAIT_TIME_GATE, self.state_close_gate)
        
    def state_close_gate(self):
        print "[CollectorController.state_close_gate]"

        self.gate.push()

        yield self.state_push_truck_standby
    
    def state_wait_truck_foot(self):
        print "[CollectorController.state_wait_truck_foot]"
        
        while not self.foot_up_switch.is_pressed():
            yield
            
        yield self.state_push_truck_away