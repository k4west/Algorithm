from collections import deque


ans = 0
D = ((-1, 0), (1, 0), (0, 1))
B, N, M = map(int, input().split())

# 직원마다 인접한 위치의 컨베이어 벨트를 1차원 리스트 관리
worker = [[] for _ in range(3*B-2)]
last = 0
conner = {B-2: B, B: B-2, 2*B-3: 2*B-1, 2*B-1: 2*B-3}

for _ in range(N):
    r, c, t = map(int, input().split())

    for dr, dc in D:
        nr, nc = r+dr, c+dc
        if nr == 0 or nr == B-1 or nc == B-1:   # 인접한 벨트가 있으면
            if nr == B-1:
                p = 3*B-nc-3
            else:
                p = nr + nc
            worker[p] = [0, t]   # 일 시작 가능 시간, 위치, 순번
            if last < p:
                last = p

present = deque([])
for m in range(M+3*B-3):  # 모든 선물이 다 지날 때 까지
    # 선물 M개가 모두 시작 지점에 오르고 나면, 시작 지점에는 더 이상 새로운 선물이 놓이지 않는다.
    if m < M:
        present.append(m)  # 벨트에 올라온 시간
    elif not present:
        break

    for _ in range(len(present)):   # 벨트 위에 올라온 선물만 확인
        cur = present.popleft()     # 벨트 위에 더 오래 올려져 있던 선물부터
        pos = m-cur                 # 현재 선물의 위치

        # 포장되지 않은 선물이 벨트의 끝 지점을 지나면 그 선물은 벨트에서 떨어져 폐기된다.
        if pos > last:              # 벨트 바깥 또는 더 이상 일할 사람이 없음
            continue

        if not worker[pos]:         # 현재 자리에 일할 사람이 없으면
            present.append(cur)
            continue

        s, t = worker[pos]
        if s <= m:                      # 포장이 끝나면 바로 다른 선물을 포장할 수 있음
            ans += 1
            worker[pos][0] = m + t  # 다음 가능 시작 시간 업데이트
            if pos in conner:
                worker[conner[pos]][0] = m + t  # 두 군데 인접한 직원이면 일 시작 가능 시간 업데이트 같이 해줘야 함.
        else:                           # 일하는 중 -> 포장 x
            present.append(cur)

print(ans)     # 몇 개의 선물을 팬들에게 전달할 수 있을까?
