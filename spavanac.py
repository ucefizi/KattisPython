tab = [int(i) for i in input().split()]
if tab[1] >= 45 : tab[1] -= 45
elif tab[0] != 0 :
	tab[0] -= 1
	tab[1] += 15
else :
	tab[0] = 23
	tab[1] += 15
print(tab[0], tab[1])