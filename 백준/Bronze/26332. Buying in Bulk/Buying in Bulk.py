for _ in range(int(input())):
    n, p = map(int, input().split())
    print(n, p)
    print(n*p - 2*(n-1))