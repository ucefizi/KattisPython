# Problem statement: https://open.kattis.com/problems/kemija08

tabv = ['a', 'e', 'i', 'o', 'u']
strg = input()
for i in range(len(strg) - 2):
	if strg[i] in tabv and strg[i+1] == 'p' and strg[i+2] == strg[i]:
		strg = strg[:i+1] + '--' + strg[i+3:]
tabt = strg.split('--')
strg = ''
for i in tabt:
	strg += i
print(strg)
