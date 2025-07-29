import sys
sys.setrecursionlimit(10**6)


def dfs(r, c):
    for dr, dc in d:
        nr, nc = r+dr, c+dc
        if 0 <= nr < N and 0 <= nc < M and graph[nr][nc] >= T:
            graph[nr][nc] = -1
            dfs(nr, nc)


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