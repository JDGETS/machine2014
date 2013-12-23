from collector.rail import Rail
from device import Piston, Switch
from lib import config

r = Rail()

r.slide_to_home();

r.slide_to_wait_for_sorting_position();
