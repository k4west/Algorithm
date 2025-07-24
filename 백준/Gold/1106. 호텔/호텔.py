C, N = map(int, input().split())
INF = float('inf')
dp = [INF] * (C+101)
arr = []
for _ in range(N):
    c, n = map(int, input().split())
    dp[n] = min(c, dp[n])
    arr.append((c, n))
for i in range(1, C+101):
    for c, n in arr:
        if i > n:
            dp[i] = min(dp[i-n] + c, dp[i])
print(min(dp[C:]))
