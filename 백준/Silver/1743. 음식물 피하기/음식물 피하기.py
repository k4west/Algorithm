def bfs(r, c):
    q, nq = [(r, c)], []
    cnt = 1
    while q:
        for r, c in q:
            for dr, dc in d:
                nr, nc = r+dr, c+dc
                if 0 <= nr < N and 0 <= nc < M and passage[nr][nc]:
                    passage[nr][nc] = 0
                    nq.append((nr, nc))
                    cnt += 1
        q, nq = nq, []
    return cnt


d = ((-1, 0), (1, 0), (0, -1), (0, 1))
N, M, K = map(int, input().split())
passage = [[0]*M for _ in range(N)]
for _ in range(K):
    r, c = map(int, input().split())
    passage[r-1][c-1] = 1


A = 1
for r in range(N):
    for c in range(M):
        if passage[r][c]:
            passage[r][c] = 0
            t = bfs(r, c)
            if A < t:
                A = t
print(A)
