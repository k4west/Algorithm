def main():
    t = []
    n, *p = map(int,open(0).read().split())
    d = ((-1, 0), (1, 0), (0, -1), (0, 1))
    max_level = max(p)
    graph = []
    for level in range(max_level):
        v = [0 for _ in range(n*n)]
        m = 0
        for i in range(n*n):
            if p[i] > level and not v[i]:
                m += 1
                v[i] = 1
                q, nq = [i], []
                while q or nq:
                    for j in q:
                        r, c = j//n, j%n
                        for dr, dc in d:
                            if 0<=(nr:=r+dr)<n and 0<=(nc:=c+dc)<n and p[(nj:=n*nr+nc)] > level and not v[nj]:
                                v[nj] = 1
                                nq.append(nj)
                    q, nq = nq, []
        t.append(m)
    print(max(t))
main()