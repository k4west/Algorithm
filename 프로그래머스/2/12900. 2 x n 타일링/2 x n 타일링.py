m=10**9+7
def solution(n):
    dp = [1,1]
    for _ in range(n-1):
        dp.append((dp[-1]+dp[-2])%m)
    return dp[-1]