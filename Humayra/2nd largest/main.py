for i in range(int(input())):
    (a,b,c) = map(int, input().split(' '))
    k = max(max(a,b), c)
    if(k==a): print(max(b,c))
    elif(k==b): print(max(a,c))
    else: print(max(a,b))