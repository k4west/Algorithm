def bfs(q, p):
    day = 0
    nq = []

    while q or nq:
        if not q:
            q, nq = nq, []
            day += 1
        r, c = q.pop()
        for dr, dc in d:
            nr, nc = r+dr, c+dc
            if 0 <= nr < N and 0 <= nc < M and not tomato[nr][nc]:
                tomato[nr][nc] = 1
                p -= 1
                nq.append((nr, nc))
    return -1 if p else day


d = ((-1, 0), (1, 0), (0, -1), (0, 1))
M, N = map(int, input().split())
tomato = []
ripen = []
unripe = 0

for r in range(N):
    *row, = map(int, input().split())
    tomato.append(row)

    for c, t in enumerate(row):
        if t == 1:
            ripen.append((r, c))
        elif not t:
            unripe += 1

print(bfs(ripen, unripe))