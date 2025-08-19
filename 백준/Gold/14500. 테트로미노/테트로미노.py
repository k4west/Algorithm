# 2:48 시작한지 68분
# 3:26 틀림
# 3:58 틀림
# 4:14 중단
# 4:37 다시..?

def bt(cnt, r, c, sm):
    global ans

    if cnt == 4:    # 4개 -> 종료
        if ans < sm:
            ans = sm
        return

    for dr, dc in d:
        nr, nc = r+dr, c+dc
        if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc]:
            visited[nr][nc] = 1
            s = graph[nr][nc]
            bt(cnt+1, r, c, sm+s)
            bt(cnt+1, nr, nc, sm+s)
            visited[nr][nc] = 0




ans = 0
d = ((-1, 0), (1, 0), (0, -1), (0, 1))
N, M = map(int, input().split())
graph = [[*map(int, input().split())] for _ in range(N)]
visited = [[0]*M for _ in range(N)]

for i in range(N):
    for j in range(M):
        # (i, j)를 포함한 최대 값 구하기 <- 이후에 포함 x
        visited[i][j] = 1
        bt(1, i, j, graph[i][j])

print(ans)
