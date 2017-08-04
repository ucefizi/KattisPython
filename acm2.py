import itertools as it
tab = [int(i) for i in input().split()]
tabn = [int(i) for i in input().split()]
if tabn[tab[1]] > 300: print(0, 0)
else:
    x = tabn[tab[1]]
    y = tabn[tab[1]]
    n = 1
    tabn = tabn[:tab[1]] + tabn[tab[1]+1:]
    for i in tabn: 
        if i >= 300: tabn.remove(i)
    tabb = [list(i) for i in it.permutations(tabn, len(tabn))]
    for i in tabb:
        for j in i:
            if y+j <= 300:
                x += x + j
                y += j
                n += 1
print(n, x)

# TLE