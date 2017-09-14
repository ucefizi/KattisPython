# Problem statement: https://open.kattis.com/problems/everywhere

for j in range(int(input())):
	n = int(input())
	tab = []
	for i in range(n):
		tab.append(input())
	print(len(list(set(tab))))
