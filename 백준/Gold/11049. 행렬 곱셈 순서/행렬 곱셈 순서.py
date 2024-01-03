import sys
input = sys.stdin.readline

INF = 2**31
N = int(input())
f = lambda: tuple(map(int, input().split()))
num = [*f()] + [f()[1] for _ in range(N-1)]
dp = [[0]*N for _ in range(N)]

for c in range(1, N):   # c: 행렬 개수
    for s in range(N-c):    # s: 시작 인덱스
        t0, e = INF, s+c    # t0: s~e 번째 행렬의 곱셈 연산 수 초기값, e: 마지막 인덱스
        for m in range(s, e):   # m: 중간 인덱스
            if t0 > (t:=dp[s][m] + num[s]*num[m+1]*num[e+1] + dp[m+1][e]):
                t0 = t
        dp[s][e] = t0

print(dp[0][N-1])