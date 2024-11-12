def main():
    d = ((-1, 0), (1, 0), (0, -1), (0, 1))
    m, n, *p = open(0).read().split()
    m, n = map(int, (m, n))
    v = [[0 for _ in range(n)] for _ in range(m)]
    q, nq = [(0, i) for i in range(n) if p[0][i]=='0'], []
    while q or nq:
        for r, c in q:
            for dr, dc in d:
                if 0<=(nr:=r+dr)<m and 0<=(nc:=c+dc)<n and p[nr][nc] =='0' and not v[nr][nc]:
                    if nr == m-1:
                        print('YES')
                        return
                    v[nr][nc] = 1
                    nq.append((nr, nc))
        q, nq = nq, []
    print('NO')
main()