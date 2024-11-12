def main():
    n, a, b, m, *p = map(int,open(0).read().split())
    root = [[] for _ in range(n+1)]
    for i in range(m): x, y = p[2*i:2*i+2]; root[x].append(y); root[y].append(x)
    v, c, q, nq = set(), 0, [a], []
    while q or nq:
        c += 1
        for node in q:
            for i in root[node]:
                if i == b: print(c); return
                if i not in v: nq.append(i); v.add(i)
        q, nq = nq, []
    print(-1)
main()