X = int(input())
dp = [X]*3*X
dp[X] = 0
for i in range(X-1, 0, -1):
    dp[i] = min(dp[i+1], dp[i*2], dp[i*3]) + 1
print(dp[1])