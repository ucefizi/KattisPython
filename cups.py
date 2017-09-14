# Problem statement: https://open.kattis.com/problems/cups

from operator import itemgetter as ig
n = int(input())
tab = []
for i in range(n):
	tab.append(input().split())
for i in range(n):
	try:
		x = int(tab[i][0])
		tab[i][0], tab[i][1] = tab[i][1], int(int(tab[i][0])/2)
	except ValueError:
		tab[i][1] = int(tab[i][1])
tab = sorted(tab, key=ig(int(1)))
for i in tab:
	print(i[0])
