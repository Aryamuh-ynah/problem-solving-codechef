for i in range(int(input())):
    (x, y, k) = map(int, input().split(' '))
    if( x*y > k):
        a = x*y-(x*y-k)
        print((int)(a/y))    
    
       
    else:
         print(x)