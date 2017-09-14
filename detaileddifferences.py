# Problem statement: https://open.kattis.com/problems/dtaileddifferences

tab = []
n = int(input())
for i in range(n):
	tab.append([input(), input(), ''])
for i in tab:
	for j in range(len(i[0])):
		if i[0][j] == i[1][j]:
			i[2] += '.'
		else:
			i[2] += '*'
for i in tab:
	print(i[0])
	print(i[1])
	print(i[2])
	print()
