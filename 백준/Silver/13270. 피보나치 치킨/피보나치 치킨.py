N = int(input())
chicken = [0] * (N+1)
a = 2; b = 1
while a <= N:
    chicken[a] = b
    a, b = a+b, a
min_dp = [i for i in chicken]
max_dp = [i for i in chicken]

for i in range(2, N+1):
    mn = min_dp[i] or N
    mx = max_dp[i]
    for j in range(2, i//2+1):
        if mn > (t:=min_dp[j]+min_dp[i-j]):
            mn = t
        if mx < (t:=max_dp[j]+max_dp[i-j]):
            mx = t
    min_dp[i] = mn
    max_dp[i] = mx
print(min_dp[N], max_dp[N])