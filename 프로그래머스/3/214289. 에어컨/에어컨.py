def solution(temperature, t1, t2, a, b, onboard):
    n = len(onboard); INF = float('inf')
    temperature += 10; t1 += 10; t2 += 10
    t3 = min(t1, temperature); t4 = max(t2, temperature)
    c = 2*(temperature > t2) - 1
    dp = [[INF for _ in range(51)] for _ in range(n)]
    dp[0][temperature] = 0
    for i in range(1, n):
        for j in range(51):
            tmp = [INF]
            if (onboard[i] and t1<=j<=t2) or not onboard[i]:
                if j == temperature: tmp.append(dp[i-1][j])
                elif t1<=j<=t2: tmp.append(dp[i-1][j] + b)
                if t3<=j+c<=t4: tmp.append(dp[i-1][j+c] + a)
                if t3<=j-c<=t4: tmp.append(dp[i-1][j-c])
            dp[i][j] = min(tmp)
    return min(dp[n-1])