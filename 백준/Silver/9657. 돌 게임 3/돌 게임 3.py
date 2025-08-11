dp = [1, 0, 1, 1]

N = int(input())
for i in range(4, N):
    dp.append(dp[i-1]+dp[i-3]+dp[i-4] != 3)

print(["CY", "SK"][dp[N-1]])