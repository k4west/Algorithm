X = int(input())
dp = [0, 0] + [X]*(X-1)
for i in range(2, X+1):
    dp[i] = min(dp[i//3] if not i % 3 else X, dp[i//2] if not i % 2 else X, dp[i-1]) + 1
print(dp[X])