import math as m
st = input()
while st != '0 0 0':
	tab = [float(i) for i in st.split()]
	print(m.pi*tab[0]**2, ((2*tab[0])**2)*(tab[2]/tab[1]))
	st = input()