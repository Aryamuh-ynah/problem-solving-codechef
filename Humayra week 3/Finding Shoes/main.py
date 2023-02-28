
for i in range(int(input())):
    (x,y)=map(int,input().split())
    if x-y<=0:
        print(x)
    else:
        print(2*x-y)