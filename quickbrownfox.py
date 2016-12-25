tab = [chr(j) for j in range(97, 123)]
n = int(input())
for i in range(n):
	tb = set(list(input().lower()))
	st = ''
	for j in tab:
		if j not in tb: st += j
	if len(st) != 0: print('missing', st)
	else: print('pangram')