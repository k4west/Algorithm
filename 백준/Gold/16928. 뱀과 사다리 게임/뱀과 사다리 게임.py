import sys
input = sys.stdin.readline

N, M = map(int, input().split())
d = {i:i for i in range(101)}
for _ in range(N+M):
    s, e = map(int, input().split())
    d[s] = e

c = 1
q, tmp = [1], []
while q or tmp:
    if not q:
        q, tmp = tmp, q
        c += 1
    a = q.pop(0)
    for i in range(6, 0, -1):
        b = a + i
        if b == 100:
            print(c)
            sys.exit()
        while b < 100:
            if d[b] == b:
                d[b] = 0
                break
            t = b
            b = d[t]
            d[t] = 0
        if b:
            tmp.append(b)