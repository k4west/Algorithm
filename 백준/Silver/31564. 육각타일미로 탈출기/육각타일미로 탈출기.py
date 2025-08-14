def bfs():
    cnt = 0  # 시작 타일 포함 x
    q, nq = [(0, 0)], []
    graph[0][0] = 1  # 방문 표시
    
    while q or nq:
        if not q:
            cnt += 1
            q, nq = nq, []

        r, c = q.pop()

        for dr, dc in d[r % 2]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < M and not graph[nr][nc]:
                if nr == N - 1 and nc == M - 1:
                    return cnt + 1  # 탈출구 타일은 포함 o

                graph[nr][nc] = 1
                nq.append((nr, nc))
    return -1   # 탈출구에 도달할 수 없을 경우 -1


d = (
    ((-1, -1), (-1, 0), (0, -1), (0, 1), (1, -1), (1, 0)),
    ((-1, 0), (-1, 1), (0, -1), (0, 1), (1, 0), (1, 1))
)
N, M, K = map(int, input().split())
graph = [[0]*M for _ in range(N)]

for _ in range(K):
    y, x = map(int, input().split())
    graph[y][x] = 1

print(bfs())