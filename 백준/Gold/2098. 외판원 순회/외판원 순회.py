import sys
input = sys.stdin.readline

INF = float("inf")
N = int(input())
M = (1 << N) - 1    # 방문 도시 표시하는 비트수
town = [tuple(map(int, input().split())) for _ in range(N)]
dp = [[-1] * (M + 1) for _ in range(N)]


def f(s, v):
    if v == M:
        # 모든 도시를 거쳐 다시 원래 도시로 돌아갈 수 있으면
        if town[s][0] != 0:
            return town[s][0]   # 값을 반환
        else:
            return INF  # 없으면 INF 반환

    if dp[s][v] != -1:  # 이미 방문한 경우에는 계산한 값 반환
        return dp[s][v]

    dp[s][v] = INF  # 이동하는 비용 초기값: INF
    for e in range(N):
        # 방문하지 않은 도시 e에 대해서, s -> e 로 갈 수 있는 경우
        if not ((b := (1 << e)) & v) and (c:=town[s][e]):
            # 최솟값으로 업데이트
            # dfs 알고리즘으로 e를 추가로 방문하는 경우를 탐색
            if dp[s][v] > (w := f(e, v | b) + c):
                dp[s][v] = w
    return dp[s][v]


print(f(0, 1))