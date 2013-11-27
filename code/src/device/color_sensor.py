import Adafruit_BBIO.ADC as ADC

ADC.setup()

class ColorSensor:
    UNKOWN = 0
    WHITE = 1
    ORANGE = 2

    def __init__(self, r_pin, g_pin, b_pin, white_val, orange_val, error):
        pass

    def get_color(self):
        return self.UNKOWN

