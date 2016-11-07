tab = [int(i) for i in input().split()]
for i in range(1, tab[2]+1) :
	if i%tab[0] == 0 and i%tab[1]==0 : print('FizzBuzz')
	elif i%tab[0] == 0 : print('Fizz')
	elif i%tab[1] == 0 : print('Buzz')
	else : print(i)