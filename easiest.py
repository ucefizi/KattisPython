# Problem statement: https://open.kattis.com/problems/easiest

x = int(input())
while x != 0:
	s = sum([int(i) for i in str(x)])
	found = False
	m = 11
	while not found:
		st = sum([int(i) for i in str(x * m)])
		if s != st:
			m += 1
		else:
			found = True
	print(m)
	x = int(input())
