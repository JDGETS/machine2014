from lib.component import Component
from device.stepper import Stepper
from lib.config import devices
from device.switch import Switch

class Rail(Component):
    LEFT = 1
    RIGHT = 0
    AWAY_POSITION = 0
    HOME_POSITION = 17000
    WAIT_FOR_SORTING_POSITION = HOME_POSITION - 1300
    CM_PER_STEP = 0.0024765
    AVERAGE_SPEED = 3/HOME_POSITION
    
    def __init__(self):
        self.stepper = Stepper(**devices["stepper_rail"])
        self.switch_home = Switch(devices["rail"]["switch_home"])
        self.switch_away = Switch(devices["rail"]["switch_away"])
        self.current_position = self.WAIT_FOR_SORTING_POSITION;


    def go_to_position(self, destination):
        steps = destination - self.current_position
        print "steps %d" % steps
        if steps == 0:
            return 0
        direction =  max(0,min(steps, 1)) #0 when going to away, 1 when going to home
        print "move of %d to %d" % (abs(steps), direction)
        self.stepper.move(abs(steps), direction)
        return abs(steps)

    def slide_to_home(self):
        distance = self.go_to_position(self.HOME_POSITION)
        self.current_position = self.HOME_POSITION
        yield self.wait(distance * self.AVERAGE_SPEED, self.check_homing)
    
    def slide_to_wait_for_sorting_position(self):
        self.go_to_position(self.WAIT_FOR_SORTING_POSITION)
        self.current_position = self.WAIT_FOR_SORTING_POSITION # no validation possible...

    def slide_to_away(self):
        distance = self.go_to_position(self.AWAY_POSITION)
        self.current_position = self.AWAY_POSITION
        yield self.wait(distance * self.AVERAGE_SPEED, self.check_away)

    def check_away(self):
        while not self.is_away():
            self.stepper.move(500, self.RIGHT)
            yield

    def check_homing(self):
        while not self.is_home():
            self.stepper.move(500, self.LEFT)
            yield

    def is_home(self):
        return self.switch_home.is_pressed()

    def is_away(self):
        return self.switch_away.is_pressed()