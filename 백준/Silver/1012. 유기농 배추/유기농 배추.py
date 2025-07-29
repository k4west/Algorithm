import sys
sys.setrecursionlimit(10000)


def dfs(r, c):
    for dr, dc in d:
        nr, nc = r+dr, c+dc
        if 0 <= nr < M and 0 <= nc < N and graph[nr][nc]:
            graph[nr][nc] = 0
            dfs(nr, nc)


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
