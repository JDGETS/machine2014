#! /usr/bin/env python
# -*- coding: utf-8 -*-
from device.switch import Switch
from camion_foot import CamionFoot
from lib import config
from rf_receiver import RFReceiver
import threading
import time
import Adafruit_BBIO.PWM as PWM
import Adafruit_BBIO.GPIO as GPIO
import sys

class Camion:

    PLACE_IN_POSITION_SWITCH_ID = "camion_in_position_switch"
    COLLECTOR_SWITCH_ID = "camion_collector_switch"
    RF_SWITCH = "camion_rf_switch"

    WATCH_FOOT_TIMEOUT = 60

    def __init__(self):
        print "[Camion.__init__]"
        self.foot = CamionFoot()

        config.devices[self.COLLECTOR_SWITCH_ID]["detect_edges"] = GPIO.BOTH
        self.collector_switch = Switch(**config.devices[self.COLLECTOR_SWITCH_ID]) #used by the truck to know when he have to drop the foot

        config.devices[self.PLACE_IN_POSITION_SWITCH_ID]["detect_edges"] = GPIO.RISING
        self.in_position_switch = Switch(**config.devices[self.PLACE_IN_POSITION_SWITCH_ID])

        self.rf_receiver = RFReceiver(**config.devices[self.RF_SWITCH])

        self.safe_lift_foot = None

    def activate_bindings(self):
        self.collector_switch.bind_rising_edge(self.drop_foot_safe)
        self.collector_switch.bind_falling_edge(self.bring_foot_up_safe)

    def stop(self):
        print "[Camion.stop] Stop camion"
        self.is_running = False
        self.foot.stop()
        PWM.cleanup()

    def force_stop(self):
        self.stop()
        sys.exit(0);

    def listen_stop_signal(self):
        time.sleep(60*14)
        self.rf_receiver.reset()
        self.rf_receiver.wait_for_signal()
        self.is_running = False
        self.bring_foot_up_safe() #Remonter le pied a la fin

    def run(self):
        self.is_running = True
        print "[Camion.run] Put camion down and wait for go_to_start_position signal"

        self.put_in_initial_position()

        print "[Camion.run] Start camion - waiting for signal"

        self.rf_receiver.wait_for_signal()
        print "[Camion.run] Signal received"

        # Removed because of other teams tests.
        stop_listener = threading.Thread(target=self.listen_stop_signal)
        stop_listener.start()

        self.activate_bindings(); #Activate the home switch bindings
        
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

    def drop_foot_safe(self):
        self.foot.drop()
        self.safe_lift_foot = threading.Thread(target=self.__watch_foot_timeout)
        self.safe_lift_foot.is_running = True
        self.safe_lift_foot.start()

    def bring_foot_up_safe(self):
        if self.safe_lift_foot:
            self.safe_lift_foot.is_running = False
            self.safe_lift_foot.stop()

        self.foot.bring_up()

    def __watch_foot_timeout(self):
        start_time = time.time()

        while self.safe_lift_foot.is_running and start_time + self.WATCH_FOOT_TIMEOUT < time.time():
            sleep(0.25)

        if self.safe_lift_foot.is_running:
            self.bring_foot_up_safe()