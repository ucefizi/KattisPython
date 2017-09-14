# Problem statement: https://open.kattis.com/problems/bela

dic = {
				'A': [11, 11],
				'K': [4, 4],
				'Q': [3, 3],
				'J': [20, 2],
				'T': [10, 10],
				'9': [14, 0],
				'8': [0, 0],
				'7': [0, 0]
}
x = input().split()
hands = []
for i in range(4*int(x[0])):
	hands.append(input())
res = 0
for i in hands:
	if i[1] == x[1]:
		res += dic[i[0]][0]
	else:
		res += dic[i[0]][1]
print(res)
