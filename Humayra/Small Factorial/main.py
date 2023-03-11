def fact(k):
    if(k==0):
        return 1
    else:
        return k*fact(k-1)
for i in range(int(input())):
    n=int(input())
    print(fact(n))