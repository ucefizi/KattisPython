def gcd(a, b):
	if b == 0: return a
	return gcd(b, a%b)

def lcm(a, b):
	return a*b // gcd(a,b)

st = input()
while st:
	tab = [int(i) for i in st.split()]
	x = tab[0]
	for i in range(1, len(tab)):
		x = lcm(x, tab[i])
	print(x)
	try: st = input()
	except: st = ''