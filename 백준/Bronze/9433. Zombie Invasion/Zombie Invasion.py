a=open(0)
for _ in range(int(next(a))):
    p = [*map(int, next(a).split())]
    r = 0
    for i in range(19):
        p[19-i], r = (p[19-i] + r) % 2, (p[19-i] + r) // 2
    p[0] += r
    print(*p)