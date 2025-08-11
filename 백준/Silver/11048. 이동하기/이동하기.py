N, M = map(int, input().split())
dp = [0]*(M+1)

for _ in range(N):
    for i, j in enumerate(map(int, input().split()), 1):
        dp[i] = max(dp[i], dp[i-1]) + j

print(dp[M])