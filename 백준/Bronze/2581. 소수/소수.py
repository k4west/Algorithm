import sys
M = int(sys.stdin.readline())
N = int(sys.stdin.readline())
s = []
t = []
for n in range(2, N+1):
    if n not in t:
        t.extend([i for i in range(n**2, N+1, n)])
        if n >= M:
            s.append(n)
if s:
    print(sum(s))
    print(s[0])
else: print('-1')