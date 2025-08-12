dp = [1, 0, 1, 0]

N = int(input())
for i in range(4, N):
    dp.append(dp[i-1] == dp[i-3] == dp[i-4] == 0)

print(["SK", "CY"][dp[N-1]])