N, *arr = map(int, open(0).read().split())
dp = [0 for _ in range(N+1)]
for i in range(N):
    M = m = arr[i]
    t = 0
    for j in range(i):
        k = arr[i-j-1]
        if M < k:
            M = k
        elif m > k:
            m = k
        if t <= (s:= M - m + dp[i-j-2]):
            t = s
    dp[i] = t
print(dp[N-1])