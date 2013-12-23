#! /usr/bin/env python
# -*- coding: utf-8 -*-
from device.switch import MagneticSwitch, Switch
from device.stepper import Stepper
from lib import config
import time

class Camion:

    CAMION_CONFIG_ID = "camion"
    COLLECTOR_SWITCH_ID = "camion_collector_switch"
    DUMP_SWITCH_ID = "camion_dump_switch"
    FOOT_SWITCH_ID = "camion_foot_switch"
    FOOT_STEPPER_ID = "camion_stepper"
    PLACE_IN_POSITION_SWITCH_ID = "camion_in_position_switch"
    DROP_FOOT_DIRECTION = 0
    LIFT_FOOT_DIRECTION = 1
    
    STATE_INITIAL_MAGNET = 1
    STATE_NO_MAGNET = 2
    STATE_FINAL_MAGNET = 3

    def __init__(self):
        print "[Camion.__init__]"
        self.config = config.devices[self.CAMION_CONFIG_ID]
        self.collector_switch = MagneticSwitch(**config.devices[self.COLLECTOR_SWITCH_ID])#used by the truck to know when he have to drop the foot
        self.dump_switch = MagneticSwitch(**config.devices[self.DUMP_SWITCH_ID]) # Useless for now
        self.foot_switch = MagneticSwitch(**config.devices[self.FOOT_SWITCH_ID]) 
        self.in_position_switch = Switch(**config.devices[self.PLACE_IN_POSITION_SWITCH_ID]);
        self.foot_stepper = Stepper(**config.devices[self.FOOT_STEPPER_ID])
        self.state = 0
        self.foot_stepper.disable_stepper(); # make it dead so it could be in starting position totaly down.

    def run(self):
        print "[Camion.run] Start camion - waiting for signal"

        self.wait_for_signal();

        print "[Camion.run] Camion started"
        
        self.put_in_start_position();

        self.is_running = True
        self.first_run = True
        while self.is_running:
            print "[Camion.run] Waiting for collector switch to be pushed"
            #if not self.collector_switch.is_pressed():
            self.collector_switch.wait_pressed()

            if not self.first_run:
                self.drop_foot();
            
            print "[Camion.run] Waiting for collector switch to be released"
            #if not self.collector_switch.is_released():
            self.collector_switch.wait_released()

            self.bring_foot_up();
            self.first_run = False

        print "[Camion.run] Camion stopped"
    
    def put_in_waiting_for_signal_position(self):
        """Wait to put in position signal here"""
        self.in_position_switch.wait_pressed()
        drop_foot()
        self.foot_stepper.move(self.LIFT_FOOT_DIRECTION,500)

    def wait_for_signal(self):
        """Wait for signal here"""
        #while ...:
        #    pass
        return

    def put_in_start_position(self):
        print "[Camion.put_in_start_position]"
        #Drop camion. Foot on floor so bring it up.
        self.foot_stepper.move(self.LIFT_FOOT_DIRECTION, self.config["stepper_start_position_ticks"])

    def drop_foot(self):
        print "[Camion.drop_foot]"
        self.state = self.STATE_INITIAL_MAGNET
        #Bring it up till it's done!
        while not self.is_done():
            self.foot_stepper.move(self.DROP_FOOT_DIRECTION, self.config["stepper_foot_complete_ticks"], self.is_done)
            while self.foot_stepper.is_moving():
                time.sleep(0.01) #It's ok, only component on the truck
                
    def bring_foot_up(self):
        print "[Camion.bring_foot_up]"
        self.state = self.STATE_INITIAL_MAGNET
        #Bring it up till it's done!
        while not self.is_done():
            self.foot_stepper.move(self.LIFT_FOOT_DIRECTION, self.config["stepper_foot_complete_ticks"], self.is_done)
            while self.foot_stepper.is_moving():
                time.sleep(0.01) #It's ok, only component on the truck
                
    def is_done(self):
        if self.foot_switch.is_pressed():
            if self.state == self.STATE_NO_MAGNET:
                self.state = self.STATE_FINAL_MAGNET
        else:
            if self.state == self.STATE_INITIAL_MAGNET:
                self.state = self.STATE_NO_MAGNET
        
        return self.state == self.STATE_FINAL_MAGNET;
