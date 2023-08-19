import sys
n, m = map(int, sys.stdin.readline().split())
d = {}
for i in range(m):
    d[sys.stdin.readline().strip()] = i
li = sorted(d.items(), key=lambda x:x[1])
for l in li[:n]:
    print(l[0])