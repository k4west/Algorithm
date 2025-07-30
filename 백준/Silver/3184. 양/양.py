def bfs(r, c):
    # 초기화
    q = [(r, c)]
    sheep = wolves = 0
    t = graph[r][c]
    if t == 'o':
        sheep += 1
    elif t == 'v':
        wolves += 1
    graph[r][c] = '#'   # 방문 표시는 해당 좌표를 울타리로 표시하기

    while q:
        r, c = q.pop(0)
        for dr, dc in d:
            nr, nc = r+dr, c+dc
            if 0 <= nr < R and 0 <= nc < C and graph[nr][nc] != '#':
                t = graph[nr][nc]
                if t == 'o':
                    sheep += 1
                elif t == 'v':
                    wolves += 1

                graph[nr][nc] = '#'
                q.append((nr, nc))

    if sheep > wolves:
        ans[0] += sheep
    else:
        ans[1] += wolves


ans = [0, 0]    # [sheep, wolves]
d = ((-1, 0), (1, 0), (0, -1), (0, 1))
R, C = map(int, input().split())
graph = [[*input()] for _ in range(R)]

for r in range(R):
    for c in range(C):
        # 울타리(=#)가 아니면 모두 탐색
        if graph[r][c] != '#':
            bfs(r, c)
print(*ans)
