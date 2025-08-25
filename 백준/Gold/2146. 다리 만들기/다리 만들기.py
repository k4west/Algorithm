D = ((-1, 0), (1, 0), (0, -1), (0, 1))


def get_boundary(r, c):
    boundaries = []
    q = [(r, c)]
    v[r][c] = 1

    while q:
        r, c = q.pop()
        flag = False
    
        for dr, dc in D:
            nr, nc = r+dr, c+dc
    
            if 0 <= nr < N and 0 <= nc < N:
                if not MAP[nr][nc]:
                    flag = True
                    continue

                if v[nr][nc]:
                    continue
    
                v[nr][nc] = 1
                q.append((nr, nc))
        
        if flag:
            boundaries.append((r, c))
    
    return boundaries


ans = 200
N = int(input())
MAP = [[*map(int, input().split())] for _ in range(N)]

islands = []
v = [[0]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if MAP[i][j] and not v[i][j]:
            islands.append(get_boundary(i, j))

I = len(islands)
for i in range(I):
    for x, y in islands[i]:
        for j in range(i+1, I):
            for z, w in islands[j]:
                dist = abs(x-z)+abs(y-w)-1
                if ans > dist:
                    ans = dist

print(ans)
