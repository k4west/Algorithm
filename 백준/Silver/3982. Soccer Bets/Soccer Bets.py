a = open(0)
for _ in range(int(next(a))):
    candi, dump = set(), set()
    for _ in range(16):
        t1, t2, g1, g2 = next(a).split()
        if int(g1) < int(g2):
            t1, t2 = t2, t1
        if not t1 in dump:
            candi.add(t1)
        candi.discard(t2)
        dump.add(t2)
    print(*candi)