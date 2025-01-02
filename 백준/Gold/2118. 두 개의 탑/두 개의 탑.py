N, *a = map(int, open(0).read().split())
dp = [0 for _ in range(2*N+1)]
for i in range(2*N):
    dp[i+1] = dp[i] + a[i%N]
ans = 0
t = dp[N]
e = 1
for s in range(2*N):
    while e < 2*N+1 and (tt:=dp[e] - dp[s]) <= t - tt:
        if ans < tt:
            ans = tt
        e += 1
print(ans)