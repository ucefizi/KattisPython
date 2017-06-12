tab = [int(i) for i in input().split()]
x = sum([2**i for i in range(tab[1] + 1)])
if tab[0] <= x: print('yes')
else: print('no')