# Problem statement: https://open.kattis.com/problems/dicecup

tab = [int(i) for i in input().split()]
taba = list(range(1, tab[0]+1))
tabb = list(range(1, tab[1]+1))
tabx = []
tabr = []
for i in taba:
	for j in tabb:
		tabx.append(i+j)
for i in range(2, tab[0]+tab[1]+1):
	tabr.append(tabx.count(i))
z = max(tabr)
tb = [i for i, x in enumerate(tabr) if x == z]
for i in tb:
	print(i+2)
