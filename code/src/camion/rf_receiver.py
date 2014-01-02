from device import Switch
import time

class RFReceiver:
    TIME_WINDOW = 5.0 # 5 seconds

    def __init__(self, pin):
        self.switch = Switch(pin=pin, detect_edges=GPIO.RISING)
        self.rising_edges = []

    def wait_for_signal(self):
        self.switch.bind_rising_edge(self.__on_rising_edge)

        while len(self.rising_edges) < 3:
            time.sleep(0.1)

    def __on_rising_edge(self):
        # clean up expired rising edge
        expiration = time.time() - self.TIME_WINDOW
        self.rising_edges[:] = [edge in self.rising_edges if edge > expiration]

        self.rising_edges.append(time.time())

