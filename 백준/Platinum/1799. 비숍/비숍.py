def bt(n, cnt, li):
    global max_b

    if cnt + M - n <= max_b:
        return

    if n == M:
        if max_b < cnt:
            max_b = cnt
        return

    r, c = li[n]
    if not v1[r+c] and not v2[r-c]:
        v1[r+c] = 1
        v2[r-c] = 1
        bt(n+1, cnt+1, li)
        v1[r+c] = 0
        v2[r-c] = 0
    bt(n+1, cnt, li)


N = int(input())
b1, b2 = [], []
v1, v2 = [0]*2*N, [0]*2*N

for r in range(N):
    for c, k in enumerate(map(int, input().split())):
        if k:
            if (r+c) % 2:
                b1.append((r, c))
            else:
                b2.append((r, c))

max_b = 0
M = len(b1)
bt(0, 0, b1)

t, max_b = max_b, 0
M = len(b2)
bt(0, 0, b2)

print(max_b + t)
