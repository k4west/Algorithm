def solution(land):
    dp=land[0]
    for row in land[1:]:
        tmp=[0,0,0,0]
        for i in range(4): 
            tmp[i] = max(dp[:i]+dp[i+1:])+row[i]
        dp=tmp
    return max(dp)