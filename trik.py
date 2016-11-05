strg = input()
x = 1
for i in strg :
    if i == "A" and x == 1 : x = 2
    elif i == "A" and x == 2 : x = 1
    elif i == "B" and x == 2 : x = 3
    elif i == "B" and x == 3 : x = 2
    elif i == "C" and x == 1 : x = 3
    elif i == "C" and x == 3 : x = 1
print(x)