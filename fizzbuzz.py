# Problem statement: https://open.kattis.com/problems/fizzbuzz

tab = [int(i) for i in input().split()]
for i in range(1, tab[2]+1):
	st = ''
	if i%tab[0] == 0:
		st += 'Fizz'
	if i%tab[1] == 0:
		st += 'Buzz'
	if st:
		print(st)
	else:
		print(i)
