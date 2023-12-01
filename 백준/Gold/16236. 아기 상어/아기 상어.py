import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
sea = [list(map(int, input().split())) for _ in range(N)]
for i in range(N):
    for j in range(N):
        if sea[i][j] == 9:
            start = [i, j]
            break

t = 0
def search(i, j):
    q = deque([(i, j)])
    v = [[0]*N for _ in range(N)]
    tmp = []
    v[i][j] = 1
    while q:
        r, c = q.popleft()
        if (nr:=r-1) >= 0 and (k:=sea[nr][c]) <= level and not v[nr][c]:
            if 0 < k < level:
                v[nr][c] = v[r][c] + 1
                tmp.append((v[r][c], nr, c))
            else: 
                q.append((nr, c))
                v[nr][c] = v[r][c] + 1
        if (nc:=c-1) >= 0 and (k:=sea[r][nc]) <= level and not v[r][nc]:
            if 0 < k < level:
                v[r][nc] = v[r][c] + 1
                tmp.append((v[r][c], r, nc))
            else: 
                q.append((r, nc))
                v[r][nc] = v[r][c] + 1
        if (nc:=c+1) < N and (k:=sea[r][nc]) <= level and not v[r][nc]:
            if 0 < k < level:
                v[r][nc] = v[r][c] + 1
                tmp.append((v[r][c], r, nc))
            else: 
                q.append((r, nc))
                v[r][nc] = v[r][c] + 1
        if (nr:=r+1) < N and (k:=sea[nr][c]) <= level and not v[nr][c]:
            if 0 < k < level:
                v[nr][c] = v[r][c] + 1
                tmp.append((v[r][c], nr, c))
            else: 
                q.append((nr, c))
                v[nr][c] = v[r][c] + 1
    return sorted(tmp, key=lambda x: (x[0], x[1], x[2]))


level, exp = 2, 0
i, j = start
while True:
    if not (s:=deque(search(i, j))):
        break
    sea[i][j] = 0
    k, i, j = s.popleft()
    t += k

    exp += 1
    if exp == level:
        level += 1
        exp = 0

print(t)