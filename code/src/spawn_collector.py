from collector import Collector

def start():
    print "[spawn_collector] Start collector"
    collector = Collector()
    collector.run()
    print "[spawn_collector] Stop collector"

def stop():
    collector.stop()
