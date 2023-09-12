import sys
N, M = map(int, sys.stdin.readline().split())
t = map(int, sys.stdin.readline().split())
li = [0]
for n in t:
    li.append(n+li[-1])
for _ in range(M):
    s, e = map(int, sys.stdin.readline().split())
    print(li[e]-li[s-1])