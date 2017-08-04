st = input()
i = 1
while st != '':
	tab = [int(i) for i in st.split()]
	tab = tab[1:]
	print('Case {}: {} {} {}'.format(i, min(tab), max(tab), max(tab)-min(tab)))
	i += 1
	try: st = input()
	except: st = ''