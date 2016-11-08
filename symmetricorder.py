n = int(input())
set = 1
while n != 0 :
	tab = []
	for i in range(n): tab.append(input())
	print('SET', set)
	for j in range(n) :
		if j%2 == 0 : print(tab[j])
	for k in range(n-1, -1, -1) :
		if k%2 != 0 : print(tab[k])
	n = int(input())
	set += 1