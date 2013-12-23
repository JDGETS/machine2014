from threading import Thread, Event
import Adafruit_BBIO.GPIO as GPIO
import bbio

class Stepper(Thread):

    def __init__(self, pin, direction, reset, enable, ramp_step):
        Thread.__init__(self)

        self.default_ramp_step = ramp_step
        self.pin = pin
        self.kill_evt = Event()
        self.direction = direction
        self.reset = reset
        self.enable = enable

        self.steps = None
        self.stop_condition = None

        GPIO.setup(self.reset, GPIO.OUT)
        GPIO.setup(self.enable, GPIO.OUT)
        GPIO.setup(self.direction, GPIO.OUT)

        self.reset_stepper()

    def disable_stepper():
         GPIO.output(self.enable, GPIO.HIGH)

    def reset_stepper(self):
        """ toggle the reset pin and enable the pololu. """
        GPIO.output(self.reset, GPIO.LOW)
        GPIO.output(self.reset, GPIO.HIGH)        
        GPIO.output(self.enable, GPIO.LOW)

    #0 or 1 for direction
    def move(self, direction, steps = -1, stop_condition = None):
        """ give a new move order. reset the thread if needed. """

        print "move %d"%steps

        GPIO.output(self.direction, direction)
        if self.is_alive():
            self.stop()
        
        self.reset_stepper()

        self.steps = steps
        self.stop_condition = stop_condition or (lambda: False)

        self.start()
    
    def is_moving(self):
        return self.thread and self.thread.is_alive()

    def stop(self, event = None):
        """ stop the thread """

        print "STOP!!!"
        if self.thread:
            self.kill_evt.set()
        
        self.kill_evt.clear()
        GPIO.output(self.enable, GPIO.HIGH)

    def run(self):
        """ run this biatch """

        STOP_CONDITION_INTERVAL = 25

        bbio.pinMode(pin, bbio.OUTPUT)

        step = 0
        
        ramp_step =  self.default_ramp_step if steps == -1 else min(self.default_ramp_step, self.steps)
        ramp_sleep = 100.0
        ramp_sleep_decrement = ramp_sleep / ramp_step
        min_sleep = 100 - 32 -30

        while (step < ramp_step) and not kill_evt.isSet() and (step%STOP_CONDITION_INTERVAL != 0 \
                                                        or not self.stop_condition()):
            bbio.digitalWrite(pin,bbio.LOW)
            bbio.digitalWrite(pin,bbio.HIGH)
            step +=1
            bbio.delayMicroseconds( min_sleep + ramp_sleep - ramp_sleep_decrement)

        while (step < self.steps or self.steps == -1) and not kill_evt.isSet() and \
                (step%STOP_CONDITION_INTERVAL != 0 or not self.stop_condition()):
            bbio.digitalWrite(pin,bbio.LOW)
            bbio.digitalWrite(pin,bbio.HIGH)
            step +=1
            bbio.delayMicroseconds(min_sleep)

