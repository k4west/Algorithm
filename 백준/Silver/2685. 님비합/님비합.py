for _ in range(int(input())):
    b, x, y = map(int, input().split()); n, e = 0, 1
    while x or y: n += (x%b+y%b)%b*e; x //= b; y //= b; e *= b
    print(n)