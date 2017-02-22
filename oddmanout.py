n = int(input())
for i in range(n):
	g = int(input())
	tab = [int(j) for j in input().split()]
	for j in tab:
		if tab.count(j) == 1: x = j
	print('Case #{}: {}'.format(i+1, x))