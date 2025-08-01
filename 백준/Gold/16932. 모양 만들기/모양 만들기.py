def bfs(r, c):
    tmp = 1
    q = [(r, c)]
    li = []

    while q:
        r, c = q.pop()
        for dr, dc in d:
            if 0 <= (nr := r+dr) < N and 0 <= (nc := c+dc) < M and arr[nr][nc]:
                arr[nr][nc] = 0
                tmp += 1
                q.append((nr, nc))
                li.append((nr, nc))

    for r, c in li:
        arr[r][c] = 1

    return tmp


d = ((-1, 0), (1, 0), (0, -1), (0, 1))
N, M = map(int, input().split())
arr = [[*map(int, input().split())] for _ in range(N)]

ans = 0
for n in range(N):
    for m in range(M):
        if not arr[n][m]:
            t = bfs(n, m)
            if ans < t:
                ans = t
print(ans)