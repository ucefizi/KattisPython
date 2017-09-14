# Problem statement: https://open.kattis.com/problems/plantingtrees

n = int(input())
tab = [int(i) for i in input().split()]
tab.sort()
tab = tab[::-1]
for i in range(n):
	tab[i] += i+1
print(max(tab) + 1)
