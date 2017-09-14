# Problem statement: https://open.kattis.com/problems/estimatngtheareaofacircle

from math import pi
st = input()
while st != '0 0 0':
	tab = [float(i) for i in st.split()]
	print(pi*tab[0]**2, ((2*tab[0])**2)*(tab[2]/tab[1]))
	st = input()
