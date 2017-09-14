# Problem statement: https://open.kattis.com/problems/armystrengthhard

for i in range(int(input())):
	input()
	tb = [int(j) for j in input().split()]
	g = [int(j) for j in input().split()]
	m = [int(j) for j in input().split()]
	if max(g) >= max(m):
		print('Godzilla')
	else:
		print('MechaGodzilla')
