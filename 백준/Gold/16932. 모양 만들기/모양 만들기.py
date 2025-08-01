def bfs(r, c, p):
    tmp = 1
    q = [(r, c)]
    arr[r][c] = p
    li[p] += 1

    while q:
        r, c = q.pop()
        for dr, dc in d:
            if 0 <= (nr := r+dr) < N and 0 <= (nc := c+dc) < M and arr[nr][nc] == 1:
                arr[nr][nc] = p
                tmp += 1
                q.append((nr, nc))
                li[p] += 1

    return tmp


d = ((-1, 0), (1, 0), (0, -1), (0, 1))
N, M = map(int, input().split())
arr = [[*map(int, input().split())] for _ in range(N)]
li = [0]*((N*M+1)//2+1)

ans = 0
o = 2
for n in range(N):
    for m in range(M):
        if arr[n][m] == 1:
            t = bfs(n, m, o)
            if ans < t:
                ans = t
            o += 1


for n in range(N):
    for m in range(M):
        if not arr[n][m]:
            g = set()
            for dn, dm in d:
                if 0 <= (nn := n + dn) < N and 0 <= (nm := m + dm) < M and arr[nn][nm]:
                    g.add(arr[nn][nm])
            t = sum(li[i] for i in g) + 1
            if ans < t:
                ans = t

print(ans)
