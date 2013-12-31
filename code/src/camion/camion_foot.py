#! /usr/bin/env python
# -*- coding: utf-8 -*-
from device.switch import Switch
from device.magnetic_switch import MagneticSwitch
from device.stepper import Stepper
from lib import config
import time
import Adafruit_BBIO.PWM as PWM
import sys

class CamionFoot:
    CAMION_FOOT_CONFIG_ID = "camion_foot"
    FOOT_UP_SWITCH_ID = "camion_foot_up_switch"
    FOOT_DOWN_SWITCH_ID = "camion_foot_down_switch"
    FOOT_STEPPER_ID = "camion_stepper"
    DROP_FOOT_DIRECTION = 1
    LIFT_FOOT_DIRECTION = 0

    def __init__(self):
        print "[Camion.__init__]"
        self.config = config.devices[self.CAMION_FOOT_CONFIG_ID]

        self.stepper = Stepper(**config.devices[self.FOOT_STEPPER_ID])

        self.down_switch = Switch(**config.devices[self.FOOT_DOWN_SWITCH_ID])
        self.down_switch.bind_raising_edge(self.stepper.stop) #Stop the stepper when one of the switch is activated (works with the sequence)

        self.up_switch = Switch(**config.devices[self.FOOT_UP_SWITCH_ID])
        self.up_switch.bind_raising_edge(self.stepper.stop) #Stop the stepper when one of the switch is activated (works with the sequence)

    def stop(self):
        print "[CamionFoot.stop] Stop foot"
        self.stepper.stop()

    def go_to_initial_position(self):
        print "[CamionFoot.go_to_initial_position] Drop foot then go up a li' bit more"
        self.drop()
        self.foot_stepper.move(self.DROP_FOOT_DIRECTION, self.config["stepper_start_position_ticks"])
        while self.foot_stepper.is_moving():
            time.sleep(0.01)
        self.current_position = self.STARTING_POSITION

    def put_in_start_position(self):
        print "[CamionFoot.put_in_start_position]"
        #Drop camion. Foot on floor so bring it up.
        self.stepper.move(self.LIFT_FOOT_DIRECTION, self.config["stepper_start_position_ticks"], self.up_switch.is_pressed)

        while self.stepper.is_moving():
            time.sleep(0.01)

        self.drop() # Make sure the foot touch the ground

    def drop(self):
        print "[CamionFoot.drop]"
        #Bring it up till it's done!
        while not self.down_switch.is_pressed():
            self.stepper.move(self.DROP_FOOT_DIRECTION, self.config["stepper_complete_ticks"], self.down_switch.is_pressed)
            while self.stepper.is_moving():
                time.sleep(0.01) #It's ok, only component on the truck
            time.sleep(0.01)

    def bring_up(self):
        print "[CamionFoot.bring_up]"
        #Bring it up till it's done!
        while not self.up_switch.is_pressed():
            self.stepper.move(self.LIFT_FOOT_DIRECTION, self.config["stepper_complete_ticks"], self.up_switch.is_pressed)
            while self.stepper.is_moving():
                time.sleep(0.01) #It's ok, only component on the truck
            time.sleep(0.01)