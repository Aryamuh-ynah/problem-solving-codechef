for i in range(int(input())):
    (a, b, c) = map(int, input().split(' '))
    k={ a: "Draw", b: "Bob", c: "Alice"}
    print(k[min(min(a,b), c)])