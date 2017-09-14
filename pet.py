# Problem statement: https://open.kattis.com/problems/pet

tab = []
for i in range(5):
	tab.append(sum([int(j) for j in input().split()]))
print(tab.index(max(tab))+1, max(tab))
