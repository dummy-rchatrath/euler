'''
Euler's Method Program
'''
import csv

def Euler(function, x_init, x_final, y_init, iterations):
	steps = (x_final - x_init) / float(iterations)
	x = x_init
	y = y_init
	xd = [x_init]
	yd = [y_init]
	hd = []
	for i in range(iterations):
		y += steps * function(y)
		yd.append(y)
		x += steps
		xd.append(x)
	return (xd,yd)
if __name__ == "__main__":
	(xvals, yvals) = Euler(lambda y: .6125*y**2 - 9.81, 0, 1, 0, 100000)
	for uv in zip(xvals,yvals):
		print uv[0],uv[1]
	with open('lower_bound.csv', 'ab') as fa:
		writer = csv.writer(fa, quoting=csv.QUOTE_ALL)
		writer.writerow(zip(xvals, yvals))
	(xvals2, yvals2) = Euler(lambda y: .6125*y**2 - 9.8041, 0, 1, 0, 100000)
	for uv in zip(xvals2,yvals2):
		print uv[0],uv[1]
	with open('upper_bound.csv', 'ab') as fa:
		writer = csv.writer(fa, quoting=csv.QUOTE_ALL)
		for uv in zip(xvals2,yvals2):
			writer.writerow(uv[0],uv[1])



