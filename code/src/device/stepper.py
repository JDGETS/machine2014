from threading import Thread, Event
import Adafruit_BBIO.GPIO as GPIO
import bbio


def move_thread(kill, pin, steps=-1, stop_condition = None):
    STOP_CONDITION_INTERVAL = 25
    stop_condition = stop_condition or (lambda: False); #Default: No stop conditions
    bbio.pinMode(pin, bbio.OUTPUT)
    step = 0
    default_ramp_step =2000
    ramp_step =  default_ramp_step if steps == -1 else min(default_ramp_step, steps)
    ramp_sleep = 100.0
    ramp_sleep_decrement = ramp_sleep / ramp_step
    min_sleep = 100 - 32 

    while (step < ramp_step) and not kill.isSet() and (step%STOP_CONDITION_INTERVAL != 0 or not stop_condition()):
        bbio.digitalWrite(pin,bbio.LOW)
        bbio.digitalWrite(pin,bbio.HIGH)
        step +=1
        bbio.delayMicroseconds( min_sleep + ramp_sleep - ramp_sleep_decrement)

    while (step < steps or steps == -1) and not kill.isSet() and (step%STOP_CONDITION_INTERVAL != 0 or not stop_condition()):
        bbio.digitalWrite(pin,bbio.LOW)
        bbio.digitalWrite(pin,bbio.HIGH)
        step +=1
        bbio.delayMicroseconds(min_sleep)


class Stepper(object):
    def __init__(self, pin,direction,reset,enable):
        self.pin = pin
        self.killThread = Event()
        self.direction = direction
        self.reset = reset
        self.enable = enable
        self.thread = None
        GPIO.setup(self.reset, GPIO.OUT)
        GPIO.setup(self.enable, GPIO.OUT)
        GPIO.setup(self.direction, GPIO.OUT)
        self.reset_stepper()

    def reset_stepper(self):
        GPIO.output(self.reset, GPIO.LOW)
        GPIO.output(self.reset, GPIO.HIGH)        
        GPIO.output(self.enable, GPIO.LOW)

    #0 or 1 for direction
    def move(self, direction, steps = -1, stop_condition = None):
        print "move %d"%steps
        GPIO.output(self.direction, direction)
        if self.thread and self.thread.is_alive():
            self.stop()
        
        self.reset_stepper()
        self.thread = Thread(target = move_thread, args = (self.killThread, self.pin, steps, stop_condition))
        self.thread.start()
    
    def is_moving(self):
        return self.thread and self.thread.is_alive()

    def stop(self, event = None):
        print "STOP!!!"
        if self.thread:
            self.killThread.set()
            self.thread.join()
        self.killThread.clear()
        GPIO.output(self.enable, GPIO.HIGH)


