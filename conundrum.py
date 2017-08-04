s = input()
x = 0
for i in range(len(s)):
	if (s[i] != 'P' and i%3 == 0) or (s[i] != 'E' and i%3 ==1) or (s[i] != 'R' and i%3 == 2) : x += 1
print(x)