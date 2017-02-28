x = input()
while x != '0 0 0 0':
	tab = x.split()
	p1 = tab[:2]
	p2 = tab[2:]
	if p1[0]+p1[1] == '21' or p1[0]+p1[1] == '12':
		if p2[0]+p2[1] == '21' or p2[0]+p2[1] == '12': print('Tie.')
		else: print('Player 1 wins.')
	elif p2[0]+p2[1] == '21' or p2[0]+p2[1] == '12': print('Player 2 wins.')
	elif p1[0] == p1[1]:
		if p2[0] == p2[1]: 
			if int(p2[0]) < int(p1[0]): print('Player 1 wins.')
			elif int(p2[0]) > int(p1[0]): print('Player 2 wins.')
			else: print('Tie.')
		else: print('Player 1 wins.')
	elif p2[0] == p2[1]: print('Player 2 wins.')
	else:
		pp1 = [int(i) for i in p1]
		pp2 = [int(i) for i in p2]
		s1 = int(str(max(pp1))+str(min(pp1)))
		s2 = int(str(max(pp2))+str(min(pp2)))
		if s1 > s2: print('Player 1 wins.')
		elif s1 < s2: print('Player 2 wins.')
		else: print('Tie.')
	x = input()