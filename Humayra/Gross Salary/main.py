for i in range(int(input())):
    n=int(input())
    h=(10*n)/100
    a = (90*n)/100
    b = (98*n)/100
    if(n<1500): print(n+h+a)
    else: print(n+500+b)