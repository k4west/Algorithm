import sys
T = int(sys.stdin.readline())
for _ in range(T):
    d = {}
    n = int(sys.stdin.readline())
    for _ in range(n):
        _, t = sys.stdin.readline().split()
        d[t] = d.get(t, 0) + 1
    c = 1
    for v in d.values():
        c *= v+1
    print(c-1)