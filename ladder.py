# Problem statement: https://open.kattis.com/problems/ladder

from math import radians, ceil, sin
tab = [float(i) for i in input().split()]
print(ceil(tab[0]/sin(radians(tab[1]))))
