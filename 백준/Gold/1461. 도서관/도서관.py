# 가능한 큰 거리를 갈 때, 최대한 많이 들고 가기
# 같은 방향에 대해서만(양수 또는 음수) 한 번에 들고 가기
# 마지막에 0으로 돌아올 필요 x -> 가장 먼 곳에 갈 때,,

N, M = map(int, input().split())    # 책의 개수, 한 번에 들 수 있는 책의 개수
*xs, = map(int, input().split())    # 원 위치 정보
xs.sort()                           # 정렬

dist = m = 0                        # dist: 거리, m: 마지막에 안 돌아가도 되는 거리(최장)

# 음수 범위에 대해서 진행
for d in xs[::M]:
    if d > 0:
        break
    dist -= d*2
    if m < -d:
        m = -d

# 양수 범위에 대해서 진행
for d in xs[N-1::-M]:
    if d < 0:
        break
    dist += d*2
    if m < d:
        m = d

print(dist-m)
