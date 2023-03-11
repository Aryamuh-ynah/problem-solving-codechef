for t in range(int(input())):
    n=int(input())
    k=list(map(int, input().split(' ')))
    m = list(map(int, input().split(' ')))
    b=0
    for j in range(n):
        if k[j]==m[j]: b+=1
    print(b)