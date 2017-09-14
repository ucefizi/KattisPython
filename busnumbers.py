# Problem statement: https://open.kattis.com/problems/busnumbers

n = int(input())
tab = [int(i) for i in input().split()]
tab.sort()
tb = []
x = [tab[0]]
for i in range(1, n):
	if tab[i-1] + 1 == tab[i]:
		x.append(tab[i])
	else:
		tb.append(x)
		x = [tab[i]]
	if i == n-1:
		tb.append(x)
for i, v in enumerate(tb):
	if len(v) > 2:
		tb[i] = str(tb[i][0]) + '-' + str(tb[i][-1])
	elif len(v) == 2:
		tb[i] = ' '.join([str(j) for j in tb[i]])
	else:
		tb[i] = tb[i][0]

print(' '.join([str(i) for i in tb]))
