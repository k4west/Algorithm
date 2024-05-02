a = open(0)
ans = []
for _ in range(int(next(a))):
    i, pq = next(a).rstrip().split()
    p, q = map(int, pq.split('/'))
    line = 0
    r = []
    while p != 1 or q != 1:
        if p < q:
            q -= p
            r.append(False)
        else:
            p -= q
            r.append(True)
        line += 1
    j = 1
    for _ in range(p-1):
        r.append(True)
    for _ in range(q-1):
        r.append(False)
    for t in r[::-1]:
        j *= 2
        if not t:
            j -= 1
    n = 2**line - 1 + j
    ans.append(f"{i} {n}")
print("\n".join(ans))