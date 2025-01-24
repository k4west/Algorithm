a = open(0)
N, M = map(int, next(a).split())
arr = [[] for _ in range(M)]
t = 2*N*M
for _ in range(N):
    *ms, = map(int, next(a).split())
    p = 0
    for i, m in enumerate(ms):
        t += abs(m-p)
        arr[i].append(m)
        p = m
    t += p
for ns in arr:
    p = 0
    for i, n in enumerate(ns):
        t += abs(n-p)
        p = n
    t += p
print(t)