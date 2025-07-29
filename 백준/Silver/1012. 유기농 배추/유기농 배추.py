def bfs(p):
    q, nq = [p], []
    while q or nq:
        if not q:
            q, nq = nq, []
        r, c = q.pop()
        for dr, dc in d:
            nr, nc = r+dr, c+dc
            if 0 <= nr < M and 0 <= nc < N and graph[nr][nc]:
                graph[nr][nc] = 0
                nq.append((nr, nc))


ans = []
d = ((-1, 0), (1, 0), (0, -1), (0, 1))
for _ in range(int(input())):
    M, N, K = map(int, input().split())
    graph = [[0]*N for _ in range(M)]
    for _ in range(K):
        r, c = map(int, input().split())
        graph[r][c] = 1
    cnt = 0
    for x in range(M):
        for y in range(N):
            if graph[x][y]:
                graph[x][y] = 0
                bfs((x, y))
                cnt += 1
    ans.append(cnt)
print('\n'.join(map(str, ans)))