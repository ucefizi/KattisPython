def dupl(tab) :
	for i in range(len(tab)) :
		if tab[i] in (tab[:i] + tab[i+1:]) : return True
	return False
strg = input()
tabc = []
i = 0
while i<len(strg) :
	tabc.append(strg[i:i+3])
	i += 3
if dupl(tabc) : print('GRESKA')
else :
	p = 0
	k = 0
	h = 0
	t = 0
	for i in tabc :
		if i[0] == 'P' : p+=1
		elif i[0] == 'K' : k+=1
		elif i[0] == 'H' : h+=1
		elif i[0] == 'T' : t+=1
	print(13-p, 13-k, 13-h, 13-t)