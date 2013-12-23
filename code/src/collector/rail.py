from lib.component import Component
from device.stepper import Stepper
from lib.config import devices
from device.switch import Switch

class Rail(Component):
    LEFT = 1
    RIGHT = 0
    AWAY_POSITION = 0
    HOME_POSITION = 16800
    WAIT_FOR_SORTING_POSITION = HOME_POSITION - 1300
    CM_PER_STEP = 0.0024765
    AVERAGE_SPEED = 3/HOME_POSITION
    
    def __init__(self):
        super(Rail, self).__init__(self.state_sorting_position)
        self.current_position = self.WAIT_FOR_SORTING_POSITION;
        self.stepper = Stepper(**devices["stepper_rail"])
        self.switch_home = Switch(devices["rail"]["switch_home"])
        self.switch_away = Switch(devices["rail"]["switch_away"])

    def go_to_position(self, destination):
        steps = destination - self.current_position
        print "steps %d" % steps
        if steps == 0:
            return 0
        direction =  max(0,min(steps, 1)) #0 when going to away, 1 when going to home
        print "move of %d to %d" % (abs(steps), direction)
        self.stepper.move(direction,abs(steps))
        return abs(steps)
        
    def slide_to_home(self):
        self.set_state( self.state_slide_to_home );
    
    def slide_to_wait_for_sorting_position(self):
        self.set_state( self.state_slide_to_wait_for_sorting_position );

    def slide_to_away(self):
        self.set_state( self.state_slide_to_away );
        
    def state_sorting_position(self):
        yield self.state_sorting_position
        
    def state_home(self):
        yield self.state_home
        
    def state_away(self):
        yield self.state_away

    def state_slide_to_home(self):
        distance = self.go_to_position(self.HOME_POSITION)
        self.current_position = self.HOME_POSITION
        yield self.wait(distance * self.AVERAGE_SPEED, self.state_check_homing)
    
    def state_slide_to_wait_for_sorting_position(self):
        distance = self.go_to_position(self.WAIT_FOR_SORTING_POSITION)
        self.current_position = self.WAIT_FOR_SORTING_POSITION # no validation possible...
        yield self.wait(distance * self.AVERAGE_SPEED, self.state_sorting_position)

    def state_slide_to_away(self):
        distance = self.go_to_position(self.AWAY_POSITION)
        self.current_position = self.AWAY_POSITION
        yield self.wait(distance * self.AVERAGE_SPEED, self.state_check_away)

    def state_check_away(self):
        while not self.is_away():
            self.stepper.move(self.RIGHT,200)
            yield
        yield self.state_away

    def state_check_homing(self):
        while not self.is_home():
            self.stepper.move(self.LEFT,200)
            yield
        yield self.state_home

    def is_home(self):
        return self.switch_home.is_pressed()

    def is_away(self):
        return self.switch_away.is_pressed()
        
    def is_moving(self):
        return self.stepper.is_moving()