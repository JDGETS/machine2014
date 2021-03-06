import Adafruit_BBIO.ADC as ADC
from math import sqrt
import time
from lib.logger import Logger

def norm(v):
    return sqrt(v[0]**2+v[1]**2+v[2]**2)

def u(v):
    nv = norm(v)
    return map(lambda x: x/nv, v)

def compare_colors(color1, color2):
    return sqrt((color1[0]-color2[0])**2 + (color1[1]-color2[1])**2 + (color1[2]-color2[2])**2)

class ColorSensorWrapped:
    BLACK = 0
    WHITE = 1
    ORANGE = 2
    UNKNOWN = 3

    COLOR_TO_STRING = ['BLACK','WHITE','ORANGE','UNKNOWN']

    def __init__(self, a_pin, b_pin, c_pin, black_val, white_val, orange_val, min_norm):
        ADC.setup()
        self.a_pin = a_pin
        self.b_pin = b_pin
        self.c_pin = c_pin
        self.black_val = black_val
        self.white_val = white_val
        self.orange_val = orange_val
        self.min_norm = min_norm

        self.colors =  \
            [(self.BLACK, self.black_val), \
            (self.WHITE, self.white_val), \
            (self.ORANGE, self.orange_val)]

    def read_color(self):
        while True:
            color = [0,0,0]
            color[0] = ADC.read(self.a_pin)
            time.sleep(0.001);
            color[1] = ADC.read(self.b_pin)
            time.sleep(0.001);
            color[2] = ADC.read(self.c_pin)
            time.sleep(0.001);
            if all(map(lambda x: x>0.00001, color)):
                return color
            print "[color_sensor.read_color] Invalid color:", color

    def get_color(self):
        # Need to poll color twice to get last value (bug)
        for i in range(10):
            self.read_color()

        color = self.read_color()
        norm = norm(color)

        if norm < self.min_norm:
            return self.BLACK

        normalized_color = u(color)
        color_distances = map(lambda c: (c[0], compare_colors(normalized_color, c[1])), self.colors)
        best_match = sorted(color_distances, key=lambda c: c[1])[0]

        return best_match[0]

class ColorSensor(ColorSensorWrapped):
    """ To dump color hits and look for errors. FOR TEST USE ONLY. """
    def __init__(self, a_pin, b_pin, c_pin, black_val, white_val, orange_val, min_norm):
        ColorSensorWrapped.__init__(self,a_pin, b_pin, c_pin, black_val, white_val, orange_val, min_norm)

    def get_color(self):
        # Need to poll color twice to get last value (bug)
        for i in range(10):
            self.read_color()

        color = self.read_color()
        color_norm = norm(color)

        if color_norm < self.min_norm:
            return self.BLACK

        normalized_color = u(color)
        color_distances = map(lambda c: (c[0], compare_colors(normalized_color, c[1])), self.colors)
        best_match = sorted(color_distances, key=lambda c: c[1])[0]

        return_val = best_match[0]

        if not return_val in [self.BLACK, self.UNKNOWN]:
            Logger().register_color(color, color_distances, self.COLOR_TO_STRING[return_val])

        return return_val
