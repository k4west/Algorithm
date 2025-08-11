N = int(input())
dp = [1]*10

for _ in range(N-1):
    for i in range(9):
        dp[i+1] = (dp[i+1] + dp[i]) % 10007

print(sum(dp) % 10007)
