a = open(0)
ans = []
for _ in range(int(next(a))):
    candi = set()
    dump = set()
    for _ in range(16):
        t1, t2, g1, g2 = next(a).split()
        if int(g1) > int(g2):
            if not t1 in dump:
                candi.add(t1)
            candi.discard(t2)
            dump.add(t2)
        else:
            if not t2 in dump:
                candi.add(t2)
            candi.discard(t1)
            dump.add(t1)
    ans.append(*candi)
print("\n".join(ans))