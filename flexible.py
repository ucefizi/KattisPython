tab = input().split()
tab2 = [0] + [int(i) for i in input().split()] + [int(tab[0])]
res =[]
for i in range(len(tab2)) :
    for j in range(i) :
        if tab2[i] - tab2[j] not in res :   
            res.append(tab2[i] - tab2[j])
res.sort()
strg = str(res[0])
for i in range(1, len(res)) :
    strg += " " + str(res[i])
print(strg)