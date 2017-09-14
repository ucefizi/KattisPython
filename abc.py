# Problem statement: https://open.kattis.com/problems/abc

tab = [int(i) for i in input().split()]
st = input()
tab.sort()
dic = {
				'A': tab[0],
				'B': tab[1],
				'C': tab[2],
}
print(dic[st[0]], dic[st[1]], dic[st[2]])
