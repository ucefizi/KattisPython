import math as m
tab = [float(i) for i in input().split()]
print(m.ceil(tab[0]/m.sin(m.radians(tab[1]))))