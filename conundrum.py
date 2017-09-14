# Problem statement: https://open.kattis.com/problems/conundrum

s = input()
x = 0
for i, v in enumerate(s):
	if (v != 'P' and i%3 == 0) or (v != 'E' and i%3 == 1) or (v != 'R' and i%3 == 2):
		x += 1
print(x)
