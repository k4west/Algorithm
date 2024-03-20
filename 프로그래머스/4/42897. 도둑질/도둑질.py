def solution(money):
    n = len(money) - 1
    dp1 = [0 for _ in range(n)]
    dp2 = [0 for _ in range(n)]

    for i in range(n):
        dp1[i] = max(dp1[i - 1], dp1[i - 2] + money[i])
        dp2[i] = max(dp2[i - 1], dp2[i - 2] + money[i + 1])

    return max(dp1[-1], dp2[-1])