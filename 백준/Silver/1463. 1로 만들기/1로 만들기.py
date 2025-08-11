X = int(input())
dp = [0, 0] + [X]*(X-1)
for i in range(2, X+1):
    if not i % 3 and dp[i] > dp[i//3] + 1:
        dp[i] = dp[i//3] + 1
    if not i % 2 and dp[i] > dp[i//2] + 1:
        dp[i] = dp[i//2] + 1
    if dp[i] > dp[i-1] + 1:
        dp[i] = dp[i-1] + 1
print(dp[X])