st = input()
tab = list(st)
x = ''
y = 0
for i in range(len(tab)):
	if tab[i] not in st[:i]+st[i+1:]:
		x = tab[i]
		tab.remove(x)
		st = ''.join(tab)
		break
for i in range(len(tab)):
	if tab[i] not in st[:i]+st[i+1:]:
		y += 1
print(y)