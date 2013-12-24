from device import Piston

class VacuumShakerPiston(Piston):
    """Piston controller"""

    def __init__(self, pin, pull_duty, standby_duty, complete_standby_duty, push_duty):
        super(VacuumShakerPiston, self).__init__(pin, pull_duty, standby_duty, push_duty)
        self.complete_standby_duty = complete_standby_duty

    def complete_standby(self):
        """set servo to complete standby position"""
        self.set_duty(self.complete_standby_duty)