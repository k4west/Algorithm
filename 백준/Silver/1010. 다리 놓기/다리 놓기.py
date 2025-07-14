def comb(n, r):
    c = 1
    r = min(r, n-r)
    for i in range(n-r+1, n+1):
        c *= i
    for i in range(1, r+1):
        c //= i
    return c

a = []
for _ in range(int(input())):
    N, M = map(int, input().split())
    a.append(comb(M, N))
print(*a, sep='\n')