def g(n):
    f = [0, 1] + [0]*(n-1) + [1]
    for i in range(2, n+1):
        f[i] = f[i-1] + f[i-2]
    return f[n-1], f[n]

import sys
a = int(sys.stdin.readline())
for _ in range(a):
    n = int(int(sys.stdin.readline()))
    print(*g(n))
