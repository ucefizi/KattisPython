tab = [int(i) for i in input().split()]
tabn = [int(i) for i in input().split()]
if tabn[tab[1]] > 300: print(0, 0)
else:
	x = tabn[tab[1]]
	n = 1
	t = 300-x
	tabn = tabn[:tab[1]] + tabn[tab[1]+1:]
	for i in tabn: 
		if i > t: tabn.remove(i)
	tabn.sort()
	for i in tabn:
		if i <= t:
			x += x + i
			n += 1
			t -= i
	print(n, x)