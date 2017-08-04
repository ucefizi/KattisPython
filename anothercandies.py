n = int(input())
for i in range(n):
	input()
	l = int(input())
	s = 0
	for j in range(l): s += int(input())
	if not s%l: print('YES')
	else: print('NO')