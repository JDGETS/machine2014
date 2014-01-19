import device
from device.color_sensor import norm, u
from lib import config
import time

from lib import ex_pdb
ex_pdb.init()

print "==== Color calibration tool ===="

sample_size = 5

def sample_info(sample):
    norms = map(norm, sample)
    normalized_sample = map(u, sample)

    color_sum = reduce(lambda acc, c: map(sum, zip(acc,c)), normalized_sample, [0,0,0])
    color_mean = map(lambda x: x/len(normalized_sample), color_sum)
    max_distance = max(map(lambda c: device.color_sensor.compare_colors(color_mean, c), normalized_sample))
    return (color_mean, max_distance, min(norms), max(norms))

def print_sample_info(black_sample, white_sample, orange_sample):
    black_stat = sample_info(black_sample)
    white_stat = sample_info(white_sample)
    orange_stat = sample_info(orange_sample)

    print "Black: {val: %s, max_error: %f, min_norm: %f, max_norm: %f}" % black_stat
    print "White: {val: %s, max_error: %f, min_norm: %f, max_norm: %f}" % white_stat
    print "Orange: {val: %s, max_error: %f, min_norm: %f, max_norm: %f}" % orange_stat

    print "Config value: "
    print "\"black_val\": %s,\n\"white_val\": %s,\n\"orange_val\": %s,\n" % (black_stat[0], white_stat[0], orange_stat[0])

def sample_colors(color_sensor, piston = None):
    colors = []
    for i in range(sample_size):
        # Empty ADC buffer
        for i in range(10):
            color_sensor.read_color()

        # Sample color
        print "Sampling"
        for i in range(5):
            colors.append(color_sensor.read_color())

        # Push ball to get next one
        if piston:
            piston.pull()
            time.sleep(1.0)
            piston.push()
            time.sleep(1.0)
        else:
            time.sleep(1.0)
    return colors

color_sensor = device.ColorSensor(**config.devices["color_sensor"])
piston_1 = device.Piston(**config.devices["orange_piston"])
piston_2 = device.Piston(**config.devices["white_piston"])

piston_2.pull()
time.sleep(1.0)
piston_1.push()

# Calibrate void space
print "Please remove any ball in the sorter"
raw_input("Press enter to continue...")
black_sample = sample_colors(color_sensor)
print "Black calibration done"

# Calibrate white ball
print "Please insert %d whites balls" % sample_size
raw_input("Press enter to continue...")
white_sample = sample_colors(color_sensor, piston_1)
print "White calibration done"

# Calibrate orange ball
print "Please insert %d orange balls" % sample_size
raw_input("Press enter to continue...")
orange_sample = sample_colors(color_sensor, piston_1)
print "Orange calibration done"

print "==== Calibration done ===="
print_sample_info(black_sample, white_sample, orange_sample)
