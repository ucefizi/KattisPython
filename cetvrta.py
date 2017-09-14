# Problem statement: https://open.kattis.com/cetvrta

a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
c = [int(i) for i in input().split()]
d = [0, 0]
if a[0] == b[0]:
	d[0] = c[0]
elif a[0] == c[0]:
	d[0] = b[0]
else:
	d[0] = a[0]
if a[1] == b[1]:
	d[1] = c[1]
elif a[1] == c[1]:
	d[1] = b[1]
else:
	d[1] = a[1]
print(d[0], d[1])
