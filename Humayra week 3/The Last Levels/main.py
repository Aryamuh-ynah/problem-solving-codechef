for i in range(int(input())):
    (x,y,z) = map(int, input().split(' '))
    if(x%3==0):
        l=((int)((x/3)-1)*z)
        print((x*y)+l)
    else:
        
        l=((int)(x/3)*z)
        print((x*y)+l)