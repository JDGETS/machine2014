import device.stepper
import pygal
import math

class MockKill(object):
	def __init__(self):
		self.set = False
	def isSet(self):
		return self.set

class StepCollector(object):
	def __init__(self):
		self.points = []
	def do(self, t):
		self.points.append(t)

COLLECTOR = StepCollector()

class bbio_mock(object):
	LOW = 0
	HIGH = 1
	OUTPUT = -2
	def __init__(self):
		self.state = {}
		self.time = 0
		return
	def pinMode(self, pin, mode):
		self.state[pin] = self.LOW
		return
	def digitalWrite(self, pin, state):
		if self.state[pin] == self.LOW and state == self.HIGH:
			COLLECTOR.do(self.time)
		self.state[pin] = state
		return
	def delayMicroseconds(self, t):
		self.time += t
		return

device.stepper.bbio = bbio_mock()

def main():

	kill = MockKill()
	device.stepper.move_thread(kill, "PIN", steps=10000, default_ramp_step=4000)

	print repr(COLLECTOR.points)

	by = 10000
	pts = {}
	for i in range(int(math.ceil(max(COLLECTOR.points) / by))):
		pts[i] = 0
	for i in COLLECTOR.points:
		pts[int(math.floor(i/by))] += 1
	print repr(pts)

	line_chart = pygal.Line(show_dots=False, relative_to=0, zero=0, interpolate='cubic', range=(0, max(pts.values())))
	line_chart.title = 'step per time.'
	line_chart.add('PIN', pts.values())
	line_chart.render_to_file('chart.svg')

	return

if __name__ == '__main__':
	main()