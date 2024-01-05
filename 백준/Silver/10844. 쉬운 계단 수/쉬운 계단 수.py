N = int(input())
dp = [0] + [1]*9

for idx in range(2, N+1):
    tmp = [0]*10
    for n in range(10):
        if not n:
            tmp[n] = (tmp[n] + dp[1])%1_000_000_000
        elif n == 9:
            tmp[n] = (tmp[n] + dp[8])%1_000_000_000
        else:
            tmp[n] = (tmp[n] + dp[n-1] + dp[n+1])%1_000_000_000
    dp = tmp

print(sum(dp)%1_000_000_000)