def bt(n, cnt):
    global max_b

    # 가지 치기
    if cnt + (M-n+1)//2 <= max_b:    # 더 해도 안 됨; candidates 절반만 탐색해서 (M-n+1)//2
        return

    # 종료 조건
    # n+2로 두칸씩 이동하기 때문에 n이 M이 넘어갈 수 있음
    # ==가 아니라 >=
    if n >= M:                  # 모두 확인 후
        if max_b < cnt:         # 최대 값 갱신
            max_b = cnt
        return

    for r, c in candidates[n]:
        if not visited[r-c]:            # 우하향 대각선에 겹치는 게 없으면 비숍 두기
            visited[r-c] = 1            # 방문 표시
            bt(n+2, cnt+1)              # 다음 탐색
            visited[r-c] = 0            # 백트레킹

    bt(n+2, cnt)                    # 이번 좌표에는 비숍을 두지 않는 경우


# 대각선 층?이 다르면(45도 각도로 보면;;) 서로 겹치치 않아서 놓을 수 있는 수도 따로 구해서 더할 수 있음
N = int(input())
M = 2*N-1
candidates = [[] for _ in range(M)]
visited = [0]*M

# 비숍을 둘 수 있는(1) 좌표 저장
for r in range(N):
    for c, k in enumerate(map(int, input().split())):
        if k:
            # 방향(우상향)이 겹치는 좌표를 모아서 저장
            candidates[r+c].append((r, c))

# 대각선 층?별로 따로 놓을 수 있는 최대 비숍 수 구하기
# 대각선 층?별로 -> bt의 첫번째 매개 변수(cnt)는 cnt + 2로 두칸씩 이동
# -> bt(0, 0)과 bt(1, 0)으로 각각 실행
max_b = 0
bt(0, 0)

t, max_b = max_b, 0
bt(1, 0)

print(max_b + t)
