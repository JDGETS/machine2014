from lib.observable import Observable
import Adafruit_BBIO.GPIO as GPIO

class LimitSwitch():
    """Simple GPIO limit switch driver"""

    def __init__(self, id, onChange):
        """Initialize the LimitSwitch from the pin ID and the callback
        Parameters:
        id:         GPIO name used to setup and read the switch value
        onChange:   callback called when the switch value changes.
                    It takes the new switch value as its only parameter"""
        # Init pin from 'id'

        self.id = id
        GPIO.setup(self.id, GPIO.IN)
        self.onChange = onChange
        self.lastValue = None

    def update(self):
        """Must be called to poll switch value and fire callback if needed"""

        # read pin value {True, False}
        switchValue = GPIO.input(self.id)

        if switchValue != self.lastValue:
            self.onChange(state = switchValue)
            self.lastValue = switchValue