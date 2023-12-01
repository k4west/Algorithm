import sys
input = sys.stdin.readline

def search(i, j, level):
    q, nq = [(i, j)], []
    v = {(i, j)}
    tmp = []
    cnt = 1
    while q or nq:
        for r, c in q:
            for dr, dc in d:
                if 0 <= (nr:=r+dr) < N and 0 <= (nc:=c+dc) < N and (k:=sea[nr][nc]) <= level and (s:=(nr, nc)) not in v:
                    if 0 < k < level:
                        tmp.append((nr, nc))
                    else: 
                        v.add(s)
                        nq.append((nr, nc))

        if tmp:
            break
        q, nq = nq, []
        cnt += 1

    if tmp:
        tmp.sort()
        return cnt, tmp[0]
    return False

def main():
    t, level, exp = 0, 2, 0
    i, j = start
    while True:
        if not (s:=search(i, j, level)):
            break
        k, (i, j) = s
        sea[i][j] = 0
        t += k

        exp += 1
        if exp == level:
            level += 1
            exp = 0

    print(t)

if __name__ == '__main__':
    N = int(input())
    d = ((-1, 0), (0, -1), (0, 1), (1, 0))
    sea = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if sea[i][j] == 9:
                start = [i, j]
                sea[i][j] = 0
                break
    main()