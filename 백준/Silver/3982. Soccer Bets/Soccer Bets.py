a = open(0)
for _ in range(int(next(a))):
    c, d = set(), set()
    for _ in range(16):
        t1, t2, g1, g2 = next(a).split()
        if int(g1) < int(g2):
            t1, t2 = t2, t1
        if not t1 in d:
            c.add(t1)
        c.discard(t2)
        d.add(t2)
    print(*c)