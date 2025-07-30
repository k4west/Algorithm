def bfs(r, c):
    cnt = 1
    graph[r][c] = 0
    q = [(r, c)]

    while q:
        r, c = q.pop(0)
        for dr, dc in d:
            nr = r + dr
            nc = c + dc

            if 0 <= nr < N and 0 <= nc < N and graph[nr][nc]:
                cnt += 1
                graph[nr][nc] = 0
                q.append((nr, nc))
    return cnt


ans = []
d = ((-1, 0), (1, 0), (0, -1), (0, 1))
N = int(input())
graph = [[*map(int, input())] for _ in range(N)]

for i in range(N):
    for j in range(N):
        if graph[i][j]:
            ans.append(bfs(i, j))

print('\n'.join(map(str, [len(ans)]+sorted(ans))))
