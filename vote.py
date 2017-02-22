t = int(input())
for i in range(t):
	n = int(input())
	tab = []
	for j in range(n):
		tab.append(int(input()))
	x = sum(tab)
	y = max(tab)
	if tab.count(y) > 1: print('no winner')
	else:
		if float(y) > float(x)/2.0: print('majority winner', tab.index(y)+1)
		else: print('minority winner', tab.index(y)+1)