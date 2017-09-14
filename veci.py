# Problem statement: https://open.kattis.com/problems/veci

import itertools as it
x = input()
tab = [list(i) for i in it.permutations(x, len(x))]
tb = []
for i in tab:
	y = ''
	for j in i:
		y += j
	tb.append(y)
tb = list(set(tb))
tb.sort()
for i, v in enumerate(tb):
	if v == x:
		try:
			print(tb[i+1])
		except IndexError:
			print(0)
