def bfs():
    cnt = 1
    q, nq = [(0, 0)], []
    graph[0][0] = 0

    while q or nq:
        if not q:
            q, nq = nq, []
            cnt += 1

        r, c = q.pop(0)
        for dr, dc in d:
            nr, nc = r + dr, c + dc

            if nr == N-1 and nc == M-1:
                return cnt + 1

            if 0 <= nr < N and 0 <= nc < M and graph[nr][nc] == 1:
                graph[nr][nc] = 0
                nq.append((nr, nc))


ans = []
d = ((-1, 0), (1, 0), (0, -1), (0, 1))
N, M = map(int, input().split())
graph = [[*map(int, input())] for _ in range(N)]
print(bfs())
