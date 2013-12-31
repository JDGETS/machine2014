#! /usr/bin/env python
# -*- coding: utf-8 -*-
from device.switch import Switch
from device.magnetic_switch import MagneticSwitch
from camion import CamionFoot
from lib import config
import time
import Adafruit_BBIO.PWM as PWM
import sys

class Camion:

    PLACE_IN_POSITION_SWITCH_ID = "camion_in_position_switch"
    COLLECTOR_SWITCH_ID = "camion_collector_switch"
    RF_SWITCH = "camion_rf_switch"

    def __init__(self):
        print "[Camion.__init__]"
        self.foot = CamionFoot()

        self.collector_switch = Switch(**config.devices[self.COLLECTOR_SWITCH_ID])#used by the truck to know when he have to drop the foot
        self.collector_switch.bind_raising_edge(self.foot.drop)
        self.collector_switch.bind_falling_edge(self.foot.bring_up)

        self.in_position_switch = Switch(**config.devices[self.PLACE_IN_POSITION_SWITCH_ID])
        self.rf_switch = Switch(**config.devices[self.RF_SWITCH])

    def stop(self):
        print "[Camion.stop] Stop camion"
        self.is_running = False
        self.foot.stop()
        PWM.cleanup()

    def force_stop(self):
        self.stop()
        sys.exit(0);

    def run(self):
        print "[Camion.run] Put camion down and wait for go_to_start_position signal"

        self.put_in_initial_position()

        print "[Camion.run] Start camion - waiting for signal"

        self.wait_for_signal();
        self.in_position_switch.bind_raising_edge(self.force_stop) # After the first push, it is now binded to stop() 

        print "[Camion.run] Camion started"

        self.put_in_start_position();

        while self.is_running:
            time.sleep(0.01)

        print "[Camion.run] Camion stopped"
    
    def put_in_initial_position(self):
        """Wait to put in position signal here"""
        print "[Camion.put_in_waiting_for_signal_position] Waiting for start switch"
        self.in_position_switch.wait_pressed()
        self.foot.go_to_initial_position()

    def wait_for_signal(self):
        """Wait for signal here"""
        print "[Camion.wait_for_signal] Waiting for RF"
        self.rf_received = False
        self.rf_switch.bind_raising_edge(self.set_received_rf)
        while not self.rf_received:
            time.sleep(0.01)
        print "[Camion.wait_for_signal] RF received"
        return

    def set_received_rf(self):
        self.rf_received = True

    def put_in_start_position(self):
        self.foot.put_in_start_position()

    def drop_foot(self):
        self.foot.drop()

    def bring_foot_up(self):
        self.foot.bring_up()