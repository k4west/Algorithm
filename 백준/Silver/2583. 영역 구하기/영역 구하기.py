def bfs(p):
    area = 1
    q, nq = [p], []
    while q or nq:
        if not q:
            q, nq = nq, []
        r, c = q.pop()
        for dr, dc in d:
            nr, nc = r+dr, c+dc
            if 0 <= nr < N and 0 <= nc < M and not graph[nr][nc]:
                graph[nr][nc] = 1
                area += 1
                nq.append((nr, nc))
    return area


ans = []
d = ((-1, 0), (1, 0), (0, -1), (0, 1))
M, N, K = map(int, input().split())
graph = [[0]*M for _ in range(N)]
for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for x in range(x1, x2):
        for y in range(y1, y2):
            graph[x][y] = 1
for x in range(N):
    for y in range(M):
        if not graph[x][y]:
            graph[x][y] = 1
            ans.append(bfs((x, y)))
print(len(ans))
print(' '.join(map(str, sorted(ans))))
