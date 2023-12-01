import sys
input = sys.stdin.readline

def main():
    N = int(input())
    sea = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if sea[i][j] == 9:
                start = [i, j]
                sea[i][j] = 0
                break

    t = 0
    def search(i, j):
        q, nq = [(i, j)], []
        v = {(i, j)}
        tmp = []
        cnt = 1
        while q or nq:
            if not q:
                if tmp:
                    break
                q, nq = nq, []
                cnt += 1

            r, c = q.pop(0)
            if (nr:=r-1) >= 0 and (k:=sea[nr][c]) <= level and (s:=(nr, c)) not in v:
                if 0 < k < level:
                    tmp.append((nr, c))
                else: 
                    v.add(s)
                    nq.append((nr, c))
            if (nc:=c-1) >= 0 and (k:=sea[r][nc]) <= level and (s:=(r, nc)) not in v:
                if 0 < k < level:
                    tmp.append((r, nc))
                else:
                    v.add(s) 
                    nq.append((r, nc))
            if (nc:=c+1) < N and (k:=sea[r][nc]) <= level and (s:=(r, nc)) not in v:
                if 0 < k < level:
                    tmp.append(( r, nc))
                else:
                    v.add(s) 
                    nq.append((r, nc))
            if (nr:=r+1) < N and (k:=sea[nr][c]) <= level and (s:=(nr, c)) not in v:
                if 0 < k < level:
                    tmp.append((nr, c))
                else:
                    v.add(s) 
                    nq.append((nr, c))
        if tmp:
            tmp.sort()
            return cnt, tmp[0]
        return False


    level, exp = 2, 0
    i, j = start
    while True:
        if not (s:=search(i, j)):
            break
        k, (i, j) = s
        sea[i][j] = 0
        t += k

        exp += 1
        if exp == level:
            level += 1
            exp = 0

    print(t)

if __name__ == "__main__":
    main()