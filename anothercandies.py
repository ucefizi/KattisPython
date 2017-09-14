# Problem statement: https://open.kattis.com/problems/anothercandies

for i in range(int(input())):
	input()
	l = int(input())
	s = 0
	for j in range(l):
		s += int(input())
	if not s%l:
		print('YES')
	else:
		print('NO')
