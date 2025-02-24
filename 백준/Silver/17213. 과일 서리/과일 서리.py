N, M = map(int, open(0).read().split())
dp = [[1] for _ in range(M)]
for i in range(M):
    for j in range(i):
        dp[i].append(dp[i-1][j]+dp[i-1][j+1])
    dp[i].append(0)
print(dp[M-1][N-1])