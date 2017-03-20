def ispal(x):
	b = bin(x)[2:]
	if b == b[::-1]: return True
	return False
n = int(input())
b = 0
x = 1
while b < n:
	if ispal(x): b += 1
	if b == n: break
	x += 2
print(x)

# TLE