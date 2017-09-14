# Problem statement: https://open.kattis.com/problems/speedlimit

n = int(input())
while n != -1:
	tabs = []
	tabt = []
	for i in range(n):
		tab = [int(i) for i in input().split()]
		tabs.append(tab[0])
		tabt.append(tab[1])
	x = tabs[0] * tabt[0]
	for i in range(1, n):
		x += tabs[i] * (tabt[i] - tabt[i - 1])
	print(x, "miles")
	n = int(input())
