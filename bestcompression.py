tab = [int(i) for i in input().split()]
tb = [2**i for i in range(tab[1] + 1)]
x = sum(tb)
if tab[0] <= x: print('yes')
else: print('no')