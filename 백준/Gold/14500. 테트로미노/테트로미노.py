def bt(cnt, r, c, sm):
    global ans
    
    if ans > sm + (4-cnt)*m:
        return

    if cnt == 4:    # 4개 -> 종료
        if ans < sm:
            ans = sm
        return

    for dr, dc in d:
        nr, nc = r+dr, c+dc
        if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc]:
            visited[nr][nc] = 1
            s = graph[nr][nc]
            bt(cnt+1, r, c, sm+s)
            bt(cnt+1, nr, nc, sm+s)
            visited[nr][nc] = 0


ans = 0
d = ((-1, 0), (1, 0), (0, -1), (0, 1))
N, M = map(int, input().split())
graph = [[*map(int, input().split())] for _ in range(N)]
m = max(sum(graph, []))
visited = [[0]*M for _ in range(N)]

for i in range(N):
    for j in range(M):
        visited[i][j] = 1
        bt(1, i, j, graph[i][j])

print(ans)
