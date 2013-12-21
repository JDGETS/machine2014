#! /usr/bin/env python
# -*- coding: utf-8 -*-
import time
from device.switch import Switch
from lib import config

class Camion:

    CAMION_CONFIG_ID = "camion"
    COLLECTOR_SWITCH_ID = "camion_collector_switch"
    DUMP_SWITCH_ID = "camion_dump_switch"
    FOOT_STEPPER_ID = "camion_stepper"

    def __init__(self):
        print "[Camion.__init__]"
        self.config = **config.devices[self.CAMION_CONFIG_ID]
        self.collector_switch = Switch(**config.devices[self.COLLECTOR_SWITCH_ID])
        self.dump_switch = Switch(**config.devices[self.DUMP_SWITCH_ID]) # Useless for now
        self.foot_stepper = Stepper(**config.devices[self.FOOT_STEPPER_ID])

    def run(self):
        print "[Camion.run] Start camion - waiting for signal"

        self.wait_for_signal();

        print "[Camion.run] Camion started"
        
        self.put_in_start_position();

        self.is_running = True
        self.first_run = True
        while self.is_running:
            if not (self.first_run and self.collector_switch.is_pressed()):
                self.collector_switch.wait_pushed()

            self.drop_foot();

            time.sleep( self.config.foot_standby_time )
            
            self.bring_foot_up();
            
            self.first_run = False

        print "[Camion.run] Camion stopped"
        
    def wait_for_signal(self):
        """Wait for signal here"""
        #while ...:
        #    pass
        return

    def put_in_start_position(self):
        #Drop camion. Foot on floor so bring it up.
        stepper.move(self.config.stepper_start_position_ticks, 1)
        return

    def drop_foot(self):
        stepper.move(self.config.stepper_foot_complete_ticks, 0)
        #If the switch isnt on, continue bringing it up a few ticks (5%) at the time

    def bring_foot_up(self):
        stepper.move(self.config.stepper_foot_complete_ticks, 1)
        #If the switch isnt on, continue bringing it up a few ticks (5%) at the time
        
