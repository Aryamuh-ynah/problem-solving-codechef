for i in range(int(input())):
    k=list(map(int, input().split(' ')))
    a=0
    s=0
    for n in k:
        if(n==0): a+=1
        else: s+=1
    if(a<s): print('yes')
    else: print('No')