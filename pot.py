# Problem statement: https://open.kattis.com/problems/pot

n = int(input())
tab = []
for i in range(n):
	tab.append(input())
x = 0
for i in tab:
	x += int(i[:-1]) ** int(i[-1:])
print(x)
