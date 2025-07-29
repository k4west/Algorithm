# 빈 격자를 탐색해 가면서 인접한 치즈가 있는 지 확인
# 빈 격자는 방문 후 -1로 표시
# 치즈를 발견 -> 표시를 해줌 ++
# 치즈의 2면 이상이 공기와 접촉 > 2 -> 녹음
# 치즈가 녹은 자리는 다음에 검사할 항목이 됨

def bfs(p):
    q, nq = [p], []
    cnt = 0
    while q or nq:
        if not q:
            q, nq = nq, []
            cnt += 1
        r, c = q.pop()
        for dr, dc in d:
            nr, nc = r+dr, c+dc
            if 0 <= nr < N and 0 <= nc < M:
                if not cheese[nr][nc]:
                    cheese[nr][nc] = -1
                    q.append((nr, nc))
                if cheese[nr][nc] > 0:
                    cheese[nr][nc] += 1
                    if cheese[nr][nc] > 2:
                        cheese[nr][nc] = -1
                        nq.append((nr, nc))
    return cnt


d = ((-1, 0), (1, 0), (0, -1), (0, 1))
N, M = map(int, input().split())
cheese = [[*map(int, input().split())] for _ in range(N)]
cheese[0][0] = -1
print(bfs((0, 0)))