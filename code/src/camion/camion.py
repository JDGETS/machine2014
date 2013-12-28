#! /usr/bin/env python
# -*- coding: utf-8 -*-
from device.switch import Switch
from device.magnetic_switch import MagneticSwitch
from device.stepper import Stepper
from lib import config
import time
import Adafruit_BBIO.PWM as PWM
import sys

class Camion:

    CAMION_CONFIG_ID = "camion"
    COLLECTOR_SWITCH_ID = "camion_collector_switch"
    DUMP_SWITCH_ID = "camion_dump_switch"
    FOOT_UP_SWITCH_ID = "camion_foot_up_switch"
    FOOT_DOWN_SWITCH_ID = "camion_foot_down_switch"
    FOOT_STEPPER_ID = "camion_stepper"
    PLACE_IN_POSITION_SWITCH_ID = "camion_in_position_switch"
    RF_SWITCH = "camion_rf_switch"
    DROP_FOOT_DIRECTION = 1
    LIFT_FOOT_DIRECTION = 0

    def __init__(self):
        print "[Camion.__init__]"
        self.first_run = True
        self.config = config.devices[self.CAMION_CONFIG_ID]
        self.foot_stepper = Stepper(**config.devices[self.FOOT_STEPPER_ID])
        self.collector_switch = Switch(**config.devices[self.COLLECTOR_SWITCH_ID])#used by the truck to know when he have to drop the foot
        self.collector_switch.bind_raising_edge(self.drop_foot) 
        self.collector_switch.bind_falling_edge(self.bring_foot_up) 
        self.dump_switch = MagneticSwitch(**config.devices[self.DUMP_SWITCH_ID]) # Useless for now
        self.foot_down_switch = Switch(**config.devices[self.FOOT_DOWN_SWITCH_ID]) 
        self.foot_down_switch.bind_raising_edge(self.foot_stepper.stop) #Stop the stepper when one of the switch is activated (works with the sequence)
        self.foot_up_switch = Switch(**config.devices[self.FOOT_UP_SWITCH_ID])
        self.foot_up_switch.bind_raising_edge(self.foot_stepper.stop) #Stop the stepper when one of the switch is activated (works with the sequence)
        self.in_position_switch = Switch(**config.devices[self.PLACE_IN_POSITION_SWITCH_ID])
        self.rf_switch = Switch(**config.devices[self.RF_SWITCH])
        
    def stop(self):
        print "[Camion.stop] Stop camion"
        self.is_running = False
        self.foot_stepper.stop()
        PWM.cleanup()
    
    def force_stop(self):
        self.stop()
        sys.exit(0);

    def run(self):
        print "[Camion.run] Put camion down and wait for go_to_start_position signal"

        self.put_in_waiting_for_signal_position()

        print "[Camion.run] Start camion - waiting for signal"

        self.wait_for_signal();
        self.in_position_switch.bind_raising_edge(self.force_stop) # After the first push, it is now binded to stop()
        
        print "[Camion.run] Camion started"
        
        self.put_in_start_position();

        self.is_running = True
        while self.is_running:
            time.sleep(0.01)

        print "[Camion.run] Camion stopped"
    
    def put_in_waiting_for_signal_position(self):
        """Wait to put in position signal here"""
        self.in_position_switch.wait_pressed()
        self.foot_stepper.move(self.DROP_FOOT_DIRECTION, self.config["stepper_start_position_ticks"])
        while self.foot_stepper.is_moving():
            time.sleep(0.01)

    def wait_for_signal(self):
        """Wait for signal here"""
        
        self.rf_received = False
        self.rf_switch.bind_raising_edge(self.set_received_rf)
        while not self.rf_received:
            time.sleep(0.01)
        print "[Camion.run] RF received"
        return

    def set_received_rf(self):
        self.rf_received = True

    def put_in_start_position(self):
        print "[Camion.put_in_start_position]"
        #Drop camion. Foot on floor so bring it up.
        self.foot_stepper.move(self.LIFT_FOOT_DIRECTION, self.config["stepper_start_position_ticks"], self.foot_up_switch.is_pressed)

    def drop_foot(self):
        if not self.first_run:
            print "[Camion.drop_foot]"
            #Bring it up till it's done!
            while not self.foot_down_switch.is_pressed():
                self.foot_stepper.move(self.DROP_FOOT_DIRECTION, self.config["stepper_foot_complete_ticks"], self.foot_down_switch.is_pressed)
                while self.foot_stepper.is_moving():
                    time.sleep(0.01) #It's ok, only component on the truck
                time.sleep(0.01)
                
    def bring_foot_up(self):
        print "[Camion.bring_foot_up]"
        #Bring it up till it's done!
        while not self.foot_up_switch.is_pressed():
            self.foot_stepper.move(self.LIFT_FOOT_DIRECTION, self.config["stepper_foot_complete_ticks"], self.foot_up_switch.is_pressed)
            while self.foot_stepper.is_moving():
                time.sleep(0.01) #It's ok, only component on the truck
            time.sleep(0.01)
        self.first_run = False