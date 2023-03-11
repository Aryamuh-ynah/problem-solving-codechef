for i in range(int(input())):
    n=int(input())
    a= list(map(int, input().split()))
    k=0
    for j in range(n):
        if(a[j]>=10 and a[j]<=60):
            k+=1
    print(k)