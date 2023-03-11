for i in range(int(input())):
    (a,b) = map(int, input().split(' '))
    x=100-a
    k=200-(b*2)
    if(x<k):
        print('First')
    elif(x>k):
        print('Second')
    else:
        print('Both')