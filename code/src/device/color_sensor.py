import Adafruit_BBIO.ADC as ADC

ADC.setup()

class ColorSensor:
    UNKOWN = 0
    WHITE = 1
    ORANGE = 2

    def __init__(self, r_pin, g_pin, b_pin, white_val, orange_val, error):
        self.r_pin = r_pin
        self.g_pin = g_pin
        self.b_pin = b_pin
        self.white_val = white_val
        self.orange_val = orange_val
        self.error = error



    def get_color(self):
        return self.UNKOWN

