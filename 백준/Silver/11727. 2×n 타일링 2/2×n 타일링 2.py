n = int(input())
dp = [1, 1] + [0]*(n-1)
for i in range(2, n+1):
    dp[i] = (dp[i-1] + dp[i-2]*2) % 10007
print(dp[n])