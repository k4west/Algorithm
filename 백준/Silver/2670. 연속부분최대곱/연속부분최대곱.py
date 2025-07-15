N = int(input())
fs = [float(input()) for _ in range(N)]
dp = [1 for _ in range(N)]
m = 0

for i in range(N):
    dp[i] = max(dp[i-1]*fs[i], fs[i], dp[i])
    m = max(m, fs[i])
if m < 1:
    print(f"{m:.3f}")
else:
    print(f"{max(dp):.3f}")