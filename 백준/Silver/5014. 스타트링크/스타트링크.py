INF = float('inf')

F, S, G, U, D = map(int, input().split())
floors = [INF]*(F+1)
q = []

if S == G:                                      # 이동할 필요가 없음
    floors[G] = 0
elif (S < G and U) or (S > G and D):  # bfs 초기화
    floors[S] = 0               # 각 층다마 눌러야 하는 버튼 최소 횟수를 기록할 리스트
    visited = [0] * (F + 1)     # 방문 기록; `bfs`라서 처음 도착한 층의 횟수가 최소임
    visited[S] = 1
    d = (U, -D)
    q = [S]

while q:
    cur = q.pop(0)

    for move in d:
        nxt = cur + move

        if nxt == G:
            floors[nxt] = floors[cur] + 1
            break

        if 0 < nxt <= F and not visited[nxt]:
            visited[nxt] = 1
            floors[nxt] = floors[cur] + 1
            q.append(nxt)

ans = floors[G]
if ans == INF:
    print("use the stairs")
else:
    print(floors[G])
