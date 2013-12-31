import datetime
import time
import os

class Logger(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Logger, cls).__new__(cls, *args, **kwargs)
            cls.instance.__real_init();
        return cls._instance

    def __init__(self):
        pass #Don't use this. __new__ fucks it up. Use __real_init

    def __real_init(self):
        self.is_initialized = False
        self.cycle_start_time = None

        date_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        directory = 'log/'+date_str
        if not os.path.exists(directory):
            os.makedirs(directory)
        self.balls_color = open(directory+'/color_sensor.dump', 'w')
        self.cycle_file = open(directory+'/cycles.dump', 'w')

    def initialize(self, collector):
        self.is_initialized = True
        self.collector = collector

    def register_color(self, color_read, color_distances, color_detected):
        self.balls_color.write(str(color_read)+" => "+str(color_distances)+" => "+str(color_detected)+"\n")
        self.balls_color.flush()

    def start_new_cycle(self):
        self.cycle_start_time = time.time()

    def end_current_cycle(self):
        if not self.is_initialized:
            raise Exception("You must initialize the logger! Usage: Logger().initialize(collector)")

        if self.cycle_start_time != None:
            cycle_time = time.time() - self.cycle_start_time
            balls_count = self.collector
            self.__write_cycle(cycle_time, balls_count)

    def __write_cycle(self, cycle_time, balls_count):
        self.cycle_file.write("{:.4f}".format(cycle_time)+","+str(balls_count)+"\n")
        self.cycle_file.flush()

    def __exit__(self):
        self.balls_color.close()
        self.cycle_file.close()