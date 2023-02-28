t= int(input())
for i in range(t):
    (a,b) = map(int, input().split(' '))
    k=(107*a)/100
    if(b<=k):
        print('Yes')
    else:
        print('NO')