c = int(input())
for i in range(c):
    x = [int(j) for j in input().split()]
    l, m = 100*x[0], x[1]
    
    left = []
    right = []
    for j in range(m):
        x = input().split()
        if x[1] == 'left': left.append(int(x[0]))
        else: right.append(int(x[0]))
    
    le = 0
    if len(left):
        z = left[0]
        le += 1
        for j in left[1:]:
            if z+j <= l:
                z += j
            else: 
                z = j
                le += 1
    ri = 0
    if len(right):
        z = right[0]
        ri += 1
        for j in right[1:]:
            if z+j <= l:
                z += j
            else: 
                z = j
                ri += 1
    
    if ri < le: print(2*le-1)
    else: print(2*ri)