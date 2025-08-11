def bt(n, cnt, li):
    global max_b

    if cnt + M - n <= max_b:    # 더 해도 안 됨(가지치기)
        return

    if n == M:                  # 모두 확인 후
        if max_b < cnt:         # 최대 값 갱신
            max_b = cnt
        return

    r, c = li[n]
    if not v1[r+c] and not v2[r-c]:     # 두 대각선에 겹치는 게 없으면 비숍 두기
        v1[r+c] = v2[r-c] = 1           # 방문 표시
        bt(n+1, cnt+1, li)              # 다음 탐색
        v1[r+c] = v2[r-c] = 0           # 백트레킹

    bt(n+1, cnt, li)                    # 이번 좌표에는 비숍을 두지 않는 경우


# 대각선 층?이 다르면(45도 각도로 보면;;) 서로 겹치치 않아서 
# 좌표를 따로 저장하고, 놓을 수 있는 수도 따로 구함
N = int(input())
b1, b2 = [], []
v1, v2 = [0]*2*N, [0]*2*N   # 두 대각선 방향에 겹치는 게 있는지 확인하는 방문표시용 리스트

# 비숍을 둘 수 있는(1) 좌표 저장
for r in range(N):
    for c, k in enumerate(map(int, input().split())):
        if k:
            # 대각선 층?에 따라 나눠서 저장
            if (r+c) % 2:
                b1.append((r, c))
            else:
                b2.append((r, c))

# 대각선 층?별로 따로 놓을 수 있는 최대 비숍 수 구하기
max_b = 0
M = len(b1)
bt(0, 0, b1)

t, max_b = max_b, 0
M = len(b2)
bt(0, 0, b2)

print(max_b + t)
