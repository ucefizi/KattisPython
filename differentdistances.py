# Problem statement: https://open.kattis.com/problems/differentdistances

from math import fabs
x = input()
while x != '0':
	tab = [float(i) for i in x.split()]
	x1, y1, x2, y2, p = tab[0], tab[1], tab[2], tab[3], tab[4]
	print(round(pow(pow(fabs(x1 - x2), p) + pow(fabs(y1 - y2), p), 1/p), 10))
	x = input()
