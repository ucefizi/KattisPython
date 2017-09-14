# Problem sratement: https://open.kattis.com/problems/volim

def my_next(x):
	if x == 8:
		return 1
	return x + 1

p = int(input())
n = int(input())
tab = []
t = 210
for i in range(n):
	tab.append(input().split())
for i in tab:
	if i[1] == 'T':
		t -= int(i[0])
		if t > 0:
			p = my_next(p)
		else:
			break
	else:
		t -= int(i[0])
		if t == 0:
			break
print(p)
