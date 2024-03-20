def solution(arr):
    INF = 201000
    nums = arr[0::2]
    n = len(nums)
    op = arr[1::2]
    max_dp = [[-INF for _ in range(n)] for _ in range(n)]
    min_dp = [[INF for _ in range(n)] for _ in range(n)]

    for i, v in enumerate(map(int, nums)):
        max_dp[i][i] = v
        min_dp[i][i] = v

    for nn in range(1, n):
        for i in range(n - nn):
            j = i + nn
            for k in range(i, j):
                if op[k] == "+":
                    max_dp[i][j] = max(max_dp[i][j], max_dp[i][k] + max_dp[k + 1][j])
                    min_dp[i][j] = min(min_dp[i][j], min_dp[i][k] + min_dp[k + 1][j])
                else:
                    max_dp[i][j] = max(max_dp[i][j], max_dp[i][k] - min_dp[k + 1][j])
                    min_dp[i][j] = min(min_dp[i][j], min_dp[i][k] - max_dp[k + 1][j])

    return max_dp[0][n - 1]