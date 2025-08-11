N = int(input())
stairs = [0] + [int(input()) for _ in range(N)]

dp = [0]*(N+2)
dp[1] = stairs[1]

for i in range(2, N+1):
    dp[i] = max(dp[i-2], dp[i-3] + stairs[i-1]) + stairs[i]

print(dp[N])