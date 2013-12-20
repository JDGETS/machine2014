from collector import Collector
import atexit

print "[spawn_collector] Start collector"
collector = Collector()
atexit.register(lambda: collector.stop())
collector.run()
print "[spawn_collector] Stop collector"
