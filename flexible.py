# Problem statement: https://open.kattis.com/problems/flexible

tab = input().split()
tab2 = [0] + [int(i) for i in input().split()] + [int(tab[0])]
res = []
for i, v in enumerate(tab2):
	for j in range(i):
		if v - tab2[j] not in res:
			res.append(v - tab2[j])
res.sort()
print(' '.join([str(i) for i in res]))
