from collector import Collector

collector = None

def start():
    global collector

    print "[spawn_collector] Start collector"
    collector = Collector()
    collector.run()
    print "[spawn_collector] Stop collector"

def stop():
    collector.stop()
