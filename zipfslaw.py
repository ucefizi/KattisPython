#!/usr/bin/python3.6m

import string
from sys import stdin
tab = [i for i in stdin.read().split('\nEndOfText\n') if i != '']
for i in range(len(tab)): tab[i] = tab[i].translate(str.maketrans('','', string.punctuation)).lower()
for i in tab:
	lines = [j for j in i.split('\n') if j != '']
	n = int(lines[0])
	words = []
	for j in lines[1:]: words += [k for k in j.split() if k !='']
	dic = {}
	for j in words:
		if j in dic: dic[j] += 1
		else: dic[j] = 1
	print(dic)
	out = [j for j in dic if dic[j] == n]
	out.sort()
	if not out: print('There is no such word.')
	else:
		for j in out: print(j)