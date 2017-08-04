from operator import mul
from functools import reduce as red
from math import factorial as f
strg=input()
while strg!="" :
	print(f(len(strg))//red(mul, [f(list(strg).count(i)) for i in set(strg)]))
	try :
		strg=input()
	except:
		strg=""