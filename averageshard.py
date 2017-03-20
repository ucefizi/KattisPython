t = int(input())
for i in range(t):
	input()
	x = [int(j) for j in input().split()]
	t1 = [int(j) for j in input().split()]
	t2 = [int(j) for j in input().split()]
	m1 = sum(t1)/len(t1)
	m2 = sum(t2)/len(t2)
	nb = 0
	for j in t1:
		if j < m1 and j > m2: nb += 1
	print(nb)