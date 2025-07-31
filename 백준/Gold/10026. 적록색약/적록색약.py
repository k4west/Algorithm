def bfs1(r, c):
    q = [(r, c)]
    visited[r][c] = 1

    while q:
        r, c = q.pop()
        for dr, dc in d:
            nr, nc = r+dr, c+dc
            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc] and paint[nr][nc] == color:
                visited[nr][nc] = 1
                q.append((nr, nc))


def bfs2(r, c):
    q = [(r, c)]
    visited[r][c] = 1

    while q:
        r, c = q.pop()
        for dr, dc in d:
            nr, nc = r+dr, c+dc
            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc] and paint[nr][nc] != color:
                visited[nr][nc] = 1
                q.append((nr, nc))


c1 = c2 = 0
d = ((-1, 0), (1, 0), (0, -1), (0, 1))
N = int(input())
paint = [input() for _ in range(N)]


visited = [[0]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            color = paint[i][j]
            bfs1(i, j)
            c1 += 1

visited = [[0]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            color = paint[i][j]
            if color == 'B':
                bfs1(i, j)
            else:
                color = 'B'
                bfs2(i, j)
            c2 += 1

print(c1, c2)
