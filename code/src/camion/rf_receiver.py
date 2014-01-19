from device import Switch
import time
import Adafruit_BBIO.GPIO as GPIO

class RFReceiver:
    TIME_WINDOW = 5.0 # 5 seconds
    SIGNAL_COUNT = 3

    def __init__(self, pin):
        self.switch = Switch(pin=pin, detect_edges=GPIO.RISING)
        self.rising_edges = []

    def wait_for_signal(self):
        self.switch.bind_rising_edge(self.__on_rising_edge)

        while len(self.rising_edges) < self.SIGNAL_COUNT:
            time.sleep(0.1)

    def reset(self):
        self.rising_edges = []

    def __on_rising_edge(self):
        # clean up expired rising edge
        expiration = time.time() - self.TIME_WINDOW
        self.rising_edges[:] = [edge for edge in self.rising_edges if edge > expiration]

        self.rising_edges.append(time.time())
