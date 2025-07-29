def dfs(r, c):
    stack = []
    while True:
        for dr, dc in d:
            nr, nc = r+dr, c+dc
            if 0 <= nr < N and 0 <= nc < M and graph[nr][nc] >= T:
                graph[nr][nc] = -1
                stack.append((r, c))
                r, c = nr, nc
                break
        else:
            if stack:
                r, c = stack.pop()
            else:
                break


d = ((-1, 0), (1, 0), (0, -1), (0, 1))
N, M = map(int, input().split())
graph = []
for _ in range(N):
    *rgb, = map(int, input().split())
    graph.append([sum(rgb[3*i:3*(i+1)]) for i in range(M)])
T = int(input())*3
cnt = 0
for r in range(N):
    for c in range(M):
        if graph[r][c] >= T:
            graph[r][c] = -1
            dfs(r, c)
            cnt += 1
print(cnt)