for i in range(int(input())):
    s=input()
    t=input()
    for j in range(5):
        if s[j]==t[j]: print('G', end='')
        else: print('B', end='')
    print()