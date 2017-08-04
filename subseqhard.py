for i in range(int(input())):
	input()
	n = int(input())
	tab = [int(j) for j in input().split()]
	dic = {}
	s = 0
	c = 0
	dic[0] = 1
	for j in tab:
		s += j
		if (s-47) in dic: c += dic[s-47]
		if s in dic: dic[s] += 1
		else: dic[s] = 1
	print(c)