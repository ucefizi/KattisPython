t = int(input())
for j in range(t):
	n = int(input())
	tab = []
	for i in range(n) :
		tab.append(input())
	print(len(list(set(tab))))