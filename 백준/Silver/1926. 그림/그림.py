def bfs(r, c):
    q, nq = [(r, c)], []
    cnt = 1
    while q:
        for r, c in q:
            for dr, dc in d:
                nr, nc = r+dr, c+dc
                if 0 <= nr < N and 0 <= nc < M and paint[nr][nc]:
                    paint[nr][nc] = 0
                    nq.append((nr, nc))
                    cnt += 1
        q, nq = nq, []
    return cnt


d = ((-1, 0), (1, 0), (0, -1), (0, 1))
N, M = map(int, input().split())
paint = [[*map(int, input().split())] for _ in range(N)]
A = []
for r in range(N):
    for c in range(M):
        # 그림 찾기
        if paint[r][c]:
            paint[r][c] = 0
            A.append(bfs(r, c))
print(len(A))
print(max(A) if A else 0)
