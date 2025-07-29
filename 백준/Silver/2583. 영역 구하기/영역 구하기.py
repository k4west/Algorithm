def dfs(r, c):
    cnt = 1
    stack = []
    while True:
        for dr, dc in d:
            nr, nc = r+dr, c+dc
            if 0 <= nr < N and 0 <= nc < M and not graph[nr][nc]:
                graph[nr][nc] = 1
                cnt += 1
                stack.append((r, c))
                r, c = nr, nc
                break
        else:
            if stack:
                r, c = stack.pop()
            else:
                break
    return cnt


ans = []
d = ((-1, 0), (1, 0), (0, -1), (0, 1))

M, N, K = map(int, input().split())
graph = [[0]*(M) for _ in range(N)]
for _ in range(K):
    x0, y0, x1, y1 = map(int, input().split())
    for x in range(x0, x1):
        for y in range(y0, y1):
            graph[x][y] = 1

for x in range(N):
    for y in range(M):
        if not graph[x][y]:
            graph[x][y] = 1
            ans.append(dfs(x, y))
print(len(ans))
print(*sorted(ans))
