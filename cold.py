n = int(input())
tab = [int(i) for i in input().split()]
x = 0
for i in tab :
    if i < 0 : x += 1
print(x)