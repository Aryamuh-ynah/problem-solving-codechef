for i in range(int(input())):
    (a, b, c) =  map(int, input().split(' '))
    
    k=max(max(a, b), c)
    print(k)