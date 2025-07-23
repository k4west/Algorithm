ans = []
for _ in range(int(input())):
    N = int(input())
    *coins, = map(int, input().split())
    M = int(input())
    dp = [0] * (M+1)
    dp[0] = 1
    for coin in coins:
        for m in range(M+1):
            if m >= coin:
                dp[m] += dp[m-coin] 
    ans.append(dp[M])
print(*ans, sep='\n')