N = int(input())
M = 1_000_000_000
dp = [0] + [1] * 9

for idx in range(2, N + 1):
    tmp = [dp[1]] + [0] * 8 + [dp[8]]
    for n in range(1, 9):
        tmp[n] = (dp[n - 1] + dp[n + 1]) % M
    dp = tmp

print(sum(dp) % M)