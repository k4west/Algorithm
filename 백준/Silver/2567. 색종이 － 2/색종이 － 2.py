def bfs(x, y):
    # 초기화
    q = [(x, y)]
    paper[x][y] = -1
    cnt = 0

    while q:
        r, c = q.pop(0)
        for dr, dc in d:
            nr, nc = r+dr, c+dc
            if 0 <= nr < 102 and 0 <= nc < 102:    # 도화지 내 탐색
                t = paper[nr][nc]
                if not t:               # 0이면 추가 탐색
                    q.append((nr, nc))
                    paper[nr][nc] = -1      # 방문 표시
                elif t == 1:            # 1이면 둘레 추가
                    cnt += 1
    return cnt


paper = [[0]*102 for _ in range(102)]
d = ((-1, 0), (1, 0), (0, -1), (0, 1))
ans = 0
for _ in range(int(input())):
    x, y = map(int, input().split())
    for i in range(x+1, x+11):
        for j in range(y+1, y+11):
            paper[i][j] = 1

for i in range(102):
    for j in range(102):
        if paper[i][j] == 0:
            ans += bfs(i, j)
print(ans)