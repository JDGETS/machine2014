from device import Switch
import Adafruit_BBIO.GPIO as GPIO
import sys, time

pin = sys.argv[1]
s = Switch(pin, GPIO.BOTH)

def print_rising():
    print "Rising"

def print_falling():
    print "Falling"

s.bind_rising_edge(print_rising)
s.bind_falling_edge(print_falling)

while True:
    time.sleep(1.0)
