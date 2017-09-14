# Problem statement: https://open.kattis.com/problems/compass

a = int(input())
b = int(input())
if b >= a:
	cl = b - a
	acl = 360 - b + a
else:
	acl = a - b
	cl = 360 - a + b
if cl <= acl:
	print(cl)
else:
	print(-acl)
