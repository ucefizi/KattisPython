# Problem statement: https://open.kattis.com/problems/symmetricorder

n = int(input())
st = 1
while n != 0:
	tab = []
	for i in range(n):
		tab.append(input())
	print('SET', st)
	for j in range(n):
		if j%2 == 0:
			print(tab[j])
	for k in range(n-1, -1, -1):
		if k%2 != 0:
			print(tab[k])
	n = int(input())
	st += 1
