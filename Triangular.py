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
		MOD_X = abs(x)
		F_VALUE = 1-MOD_X
		if( MOD_X <= 1 ):
			yvalues.append(F_VALUE)
		else:
			yvalues.append(0)
	matplotlib.pyplot.plot(xvalues,yvalues)
	matplotlib.pyplot.show()
values()
draw_graph()
