def solution(land):
    dp=land[0]
    for row in land[1:]:
        tmp=[0,0,0,0]
        for i, s in enumerate(row):
            tmp[i] = max(dp[:i]+dp[i+1:])+s
        dp=tmp
    return max(dp)