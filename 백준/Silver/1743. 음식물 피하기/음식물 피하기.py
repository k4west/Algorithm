import sys
sys.setrecursionlimit(10**5)


def dfs(r, c):
    cnt = 1
    for dr, dc in d:
        nr, nc = r + dr, c + dc
        if 0 <= nr < N and 0 <= nc < M and passage[nr][nc]:
            passage[nr][nc] = 0
            cnt += dfs(nr, nc)
    return cnt


d = ((-1, 0), (1, 0), (0, -1), (0, 1))
N, M, K = map(int, input().split())
passage = [[0]*M for _ in range(N)]
for _ in range(K):
    r, c = map(int, input().split())
    passage[r-1][c-1] = 1


A = []
for r in range(N):
    for c in range(M):
        if passage[r][c]:
            passage[r][c] = 0
            A.append(dfs(r, c))
print(max(A))
