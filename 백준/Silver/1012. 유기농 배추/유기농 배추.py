def dfs(r, c):
    stack = []
    while True:
        for dr, dc in d:
            nr, nc = r+dr, c+dc
            if 0 <= nr < M and 0 <= nc < N and graph[nr][nc]:
                graph[nr][nc] = 0
                stack.append((r, c))
                r, c = nr, nc
                break
        else:
            if stack:
                r, c = stack.pop()
            else:
                break


ans = []
d = ((-1, 0), (1, 0), (0, -1), (0, 1))
for _ in range(int(input())):
    M, N, K = map(int, input().split())
    graph = [[0]*N for _ in range(M)]
    for _ in range(K):
        r, c = map(int, input().split())
        graph[r][c] = 1
    cnt = 0
    for r in range(M):
        for c in range(N):
            if graph[r][c]:
                graph[r][c] = 0
                dfs(r, c)
                cnt += 1
    ans.append(cnt)
print('\n'.join(map(str, ans)))
