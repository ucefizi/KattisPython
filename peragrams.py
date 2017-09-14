# Problem statement: https://open.kattis.com/problems/peragrams

chars = [chr(i) for i in range(97, 123)]
st = list(input())
tab = [st.count(i) for i in chars]
x = 0
for i in tab:
	if i%2 != 0:
		x += 1
if x == 0:
	print(x)
else:
	print(x - 1)
