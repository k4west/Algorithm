def cross_size(r, c):
    # 십자가 크기 구하기
    dist = M+N
    for dr, dc in d:    # 사방으로 탐색
        cnt = 0
        nr, nc = r+dr, c+dc
        while 0 <= nr < N and 0 <= nc < M and graph[nr][nc] == "*":
            cnt += 1
            nr, nc = nr + dr, nc + dc
        if dist > cnt:
            dist = cnt

    # 가능한 십자가 크기에 대해서 표시
    for dr, dc in d:
        nr, nc = r, c
        for _ in range(dist):
            nr, nc = nr + dr, nc + dc
            stars[nr][nc] = 0

    return dist


def check_center(r, c):
    for dr, dc in d:
        nr, nc = r+dr, c+dc
        if not (0 <= nr < N and 0 <= nc < M and graph[nr][nc] == "*"):
            return False
    return True


ans = []
d = ((-1, 0), (1, 0), (0, -1), (0, 1))

N, M = map(int, input().split())
graph = [input() for _ in range(N)]
stars = [[0]*M for _ in range(N)]
centers = []

# 별 표시
# 십자가 중앙이 될 수 있으면 미리 표시 안 하고, 좌표를 따로 저장
for i in range(N):
    for j in range(M):
        if graph[i][j] == "*":
            if check_center(i, j):
                centers.append((i, j))
            else:
                stars[i][j] = 1

# 십자가 중심에 둘 수 있는 십자가 두고, 기록
for i, j in centers:
    k = cross_size(i, j)
    ans.append((i+1, j+1, k))

# 남은 별이 있으면, -1 출력
if sum(sum(stars, [])):
    print(-1)
else:
    print(len(ans))
    print("\n".join(" ".join(map(str, row)) for row in ans))
