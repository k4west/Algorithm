import sys
N, M= map(int, sys.stdin.readline().split())
c, t = 0, []
for _ in range(N+M):
    t.append(sys.stdin.readline())
s = set(t[:N])
li = t[N:]
for a in li:
    if a in s:
        c += 1
print(c)