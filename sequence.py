def bd(n):
	x = 2
	while x*x <= n:
		if n%x == 0: return int(n/x)
		x += 1
	return 1

n = int(input())
tb = [n]
while tb[-1] != 1:
	tb.append(bd(tb[-1]))
tab = [str(i) for i in tb]
tab = tab[::-1]
tb = [1]
while tb[-1] <= n:
	tb.append(2*tb[-1])
t = [str(i) for i in tb if i <= n]

if len(tab) >= len(t):
	print(len(tab))
	print(' '.join(tab))
else:
	print(len(t))
	print(' '.join(t))