ans = 0
B, N, M = map(int, input().split())
worker = [[] for _ in range(3*B-2)]     # 직원의 인접한 컨베이어 벨트를 1차원 리스트로 관리

# 직원이 일하는 위치에 대한 정보 정리
for _ in range(N):
    r, c, t = map(int, input().split())
    if r == 1:
        worker[c] = [0, t]          # worker[벨트 인덱스] = [시작 시간, 소요 시간]
    elif r == B-2:
        worker[3*B-3-c] = [0, t]
    if c == B-2:
        worker[r+c+1] = [0, t]

# 두개의 벨트에서 일하게 되는 상황(모서리) <- 시작 시간 공유
worker[B-2] = worker[B]
worker[2*B-3] = worker[2*B-1]

# 선물 포장
v = [0]*M   # 포장 또는 폐기 표시
for m in range(M+3*B-3):  # 모든 선물이 다 지날 때 까지
    for cur in range(min(m+1, M)):      # 벨트 위에 올라온 선물만 확인
        pos = m-cur                     # 현재 선물의 위치

        if pos > 3*B-3:                 # 벨트 바깥 -> 폐기
            v[cur] = 1
            continue

        if v[cur] or not worker[pos]:   # 포장한 거 또는 현재 자리에 일할 사람이 없으면:
            continue

        if worker[pos][0] <= m:         # 포장이 끝나면 바로 다른 선물을 포장할 수 있음
            t = worker[pos][1]
            v[cur] = 1
            ans += 1
            worker[pos][0] = m + t      # 다음 가능 시작 시간 업데이트

print(ans)     # 몇 개의 선물을 팬들에게 전달할 수 있을까?
