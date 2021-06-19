import matplotlib.pyplot
xvalues = []
yvalues = []
def values():
	RANGE_X = 0.1
	START_VALUE = -3.1
	for times in range(0,51):
		START_VALUE += RANGE_X
		xvalues.append(round(START_VALUE,2))
def draw_graph():
	for x in xvalues:
		if( (-0.5 <= x) and (x >= 0.5) ):
			yvalues.append(1)
		else:
			yvalues.append(0)
	matplotlib.pyplot.plot(xvalues,yvalues)
	matplotlib.pyplot.show()
values()
draw_graph()


