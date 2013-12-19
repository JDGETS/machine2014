import Adafruit_BBIO.ADC as ADC
from math import sqrt

ADC.setup()

def compare_colors(color1, color2):
    return sqrt((color1[0]-color2[0])**2 + (color1[1]-color2[1])**2 + (color1[2]-color2[2])**2)

class ColorSensor:
    BLACK = 0
    WHITE = 1
    ORANGE = 2
    UNKOWN = 3

    def __init__(self, a_pin, b_pin, c_pin, black_val, white_val, orange_val, error):
        self.a_pin = a_pin
        self.b_pin = b_pin
        self.c_pin = c_pin
        print self.a_pin 
        print self.b_pin 
        print self.c_pin
        self.black_val = black_val
        self.white_val = white_val
        self.orange_val = orange_val
        self.error = error

        # Must be in same order as the color constant
        self.colors = [self.black_val, self.white_val, self.orange_val]

    def read_color(self):
        while True:
            color = [ADC.read(self.a_pin), ADC.read(self.b_pin), ADC.read(self.c_pin)]
            if all(map(lambda x: x>0.00001, color)):
                return color

    def get_color(self):
        # Need to poll color twice to get last value (bug)
	for i in range(10):
            self.read_color()
        color = self.read_color()
        for i in range(3):
            if compare_colors(color, self.colors[i]) < self.error:
                return i
        return self.UNKOWN

