# Problem statement: https://open.kattis.com/problems/acm

tab = []
x = input().split()
while x[0] != '-1':
	tab.append(x)
	x = input().split()
n = 0
t = 0
for i in tab :
	if i[2] == 'right':
		n += 1
		h = i[1]
		t += int(i[0])
		for j in tab:
			if j[1] == h and j[2] == 'wrong':
				t += 20
print(n, t)
