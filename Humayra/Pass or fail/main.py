for i in range(int(input())):
    (n ,x, p) = map(int, input().split(' '))
    k=x*3-(n-x)
    if( k>=p):
        print('Pass')

    else: print('Fail')