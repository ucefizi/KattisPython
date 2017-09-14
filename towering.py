# Problem statement: https://open.kattis.com/problems/towering

tab = [int(i) for i in input().split()]
x = tab[6]
y = tab[7]
tab = tab[:6]
tab = sorted(tab)[::-1]
tabx = []
taby = []
for i in range(4):
	for j in range(i+1, 5):
		for k in range(j+1, 6):
			if tab[i]+tab[j]+tab[k] == x:
				tabx = [str(tab[i]), str(tab[j]), str(tab[k])]
			elif tab[i]+tab[j]+tab[k] == y:
				taby = [str(tab[i]), str(tab[j]), str(tab[k])]
print(' '.join(tabx), ' '.join(taby))
