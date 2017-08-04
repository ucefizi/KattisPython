tab = [int(i) for i in input().split()]
if tab[0] + tab[1] == tab[2] : print(str(tab[0]) + '+' + str(tab[1]) + '=' + str(tab[2]))
elif tab[0] - tab[1] == tab[2] : print(str(tab[0]) + '-' + str(tab[1]) + '=' + str(tab[2]))
elif tab[0] * tab[1] == tab[2] : print(str(tab[0]) + '*' + str(tab[1]) + '=' + str(tab[2]))
elif int(tab[0] / tab[1]) == tab[2] : print(str(tab[0]) + '/' + str(tab[1]) + '=' + str(tab[2]))
elif tab[0] == tab[1] + tab[2] : print(str(tab[0]) + '=' + str(tab[1]) + '+' + str(tab[2]))
elif tab[0] == tab[1] - tab[2] : print(str(tab[0]) + '=' + str(tab[1]) + '-' + str(tab[2]))
elif tab[0] == tab[1] * tab[2] : print(str(tab[0]) + '=' + str(tab[1]) + '*' + str(tab[2]))
elif tab[0] == int(tab[1] / tab[2]) : print(str(tab[0]) + '=' + str(tab[1]) + '/' + str(tab[2]))