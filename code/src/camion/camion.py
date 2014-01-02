#! /usr/bin/env python
# -*- coding: utf-8 -*-
from device.switch import Switch
from camion_foot import CamionFoot
from lib import config
from rf_receiver import RFReceiver
import time
import Adafruit_BBIO.PWM as PWM
import Adafruit_BBIO.GPIO as GPIO
import sys

class Camion:

    PLACE_IN_POSITION_SWITCH_ID = "camion_in_position_switch"
    COLLECTOR_SWITCH_ID = "camion_collector_switch"
    RF_SWITCH = "camion_rf_switch"

    def __init__(self):
        print "[Camion.__init__]"
        self.foot = CamionFoot()

        config.devices[self.COLLECTOR_SWITCH_ID]["detect_edges"] = GPIO.BOTH
        self.collector_switch = Switch(**config.devices[self.COLLECTOR_SWITCH_ID]) #used by the truck to know when he have to drop the foot

        config.devices[self.PLACE_IN_POSITION_SWITCH_ID]["detect_edges"] = GPIO.RISING
        self.in_position_switch = Switch(**config.devices[self.PLACE_IN_POSITION_SWITCH_ID])

        self.rf_receiver = RFReceiver(**config.devices[self.RF_SWITCH])

    def activate_bindings(self):
        self.collector_switch.bind_rising_edge(self.foot.drop)
        self.collector_switch.bind_falling_edge(self.foot.bring_up)

    def stop(self):
        print "[Camion.stop] Stop camion"
        self.is_running = False
        self.foot.stop()
        PWM.cleanup()

    def force_stop(self):
        self.stop()
        sys.exit(0);

    def listen_stop_signal(self):
        self.rf_receiver.reset()
        self.rf_receiver.wait_for_signal()
        self.is_running = False
        self.drop_foot()

    def run(self):
        self.is_running = True
        print "[Camion.run] Put camion down and wait for go_to_start_position signal"

        self.put_in_initial_position()

        print "[Camion.run] Start camion - waiting for signal"

        self.rf_receiver.wait_for_signal()
        print "[Camion.run] Signal received"

        stop_listener = threading.Thread(target=self.listen_stop_signal)
        stop_listener.start()

        self.activate_bindings(); #Activate the home switch bindings
        self.in_position_switch.bind_rising_edge(self.force_stop) # After the first push, it is now binded to stop()

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

    def set_received_rf(self):
        self.rf_received = True

    def put_in_start_position(self):
        self.foot.put_in_start_position()

    def drop_foot(self):
        self.foot.drop()

    def bring_foot_up(self):
        self.foot.bring_up()