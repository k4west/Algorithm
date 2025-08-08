N = int(input())
li = [float(input()) for _ in range(N)]
dp = [0]*(N+1)

for i in range(N):
    dp[i+1] = max(li[i], dp[i]*li[i])
print(f"{max(dp):.3f}")
