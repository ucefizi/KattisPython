tab = []
for i in range(10) :
	tab.append(int(input()))
tab2 = []
for i in tab :
	if i%42 not in tab2 : tab2.append(i%42)
print(len(tab2))