for i in range(int(input())):
    (a,b,c,x) = map(int, input().split(' '))
    if(a+b>=x or a+c>=x or b+c>=x):
        print('YEs')
    else:
        print('No')