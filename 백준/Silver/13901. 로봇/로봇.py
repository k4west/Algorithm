d = ((), (-1, 0), (1, 0), (0, -1), (0, 1))    # 1은 위 방향, 2은 아래 방향, 3은 왼쪽 방향, 4는 오른쪽 방향
R, C = map(int, input().split())
visited = [[0]*C for _ in range(R)]

k = int(input())
for _ in range(k):  # 장애물 방문 표시
    r, c = map(int, input().split())
    visited[r][c] = 1

r, c = map(int, input().split())
visited[r][c] = 1

*orders, = map(int, input().split())
st = set(orders)

while True:     # 맨 처음 방향으로 돌아가서 반복한다.
    for order in orders:
        dr, dc = d[order]
        nr, nc = r+dr, c+dc

        # 직진 -> 벽, 방문, 장애물 -> 다음 방향
        while 0 <= nr < R and 0 <= nc < C and not visited[nr][nc]:
            visited[nr][nc] = 1
            r, c = nr, nc
            nr, nc = r+dr, c+dc

    for idx in st:
        dr, dc = d[idx]
        nr, nc = r+dr, c+dc
        if 0 <= nr < R and 0 <= nc < C and not visited[nr][nc]:
            break
    else:    # 로봇이 움직일 수 없을 경우 동작을 멈춘다.
        break

print(r, c)
