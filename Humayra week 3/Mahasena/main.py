n=int(input())
k=0
l=0
x = list(map(int, input().split(' ')))
for i in x:
    if(i%2==0):
        k+=1
    else:
        l+=1
if(k>l):
    print('READY FOR BATTLE')
else:
    print('NOT READY')