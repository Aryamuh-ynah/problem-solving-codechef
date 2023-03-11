for i in range(int(input())):
    (m, n ,k) = map(int, input().split(' '))
    if(k*n<m):
        print('Yes')
    else:
        print('no')