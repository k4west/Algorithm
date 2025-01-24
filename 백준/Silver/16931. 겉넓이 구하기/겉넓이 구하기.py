a = open(0)
N, M = map(int, next(a).split())
arr = [[] for _ in range(M)]
t = N*M
for _ in range(N):
    *ms, = map(int, next(a).split())
    p = 0
    for i, m in enumerate(ms):
        if m > p: t += m-p
        arr[i].append(m)
        p = m
for ns in arr:
    p = 0
    for i, n in enumerate(ns):
        if n > p: t += n-p
        p = n
print(2*t)