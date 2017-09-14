# Problem statement: https://open.kattis.com/problems/bestcompression

tab = [int(i) for i in input().split()]
x = 2**(tab[1]+1) - 1
if tab[0] <= x:
	print('yes')
else:
	print('no')
