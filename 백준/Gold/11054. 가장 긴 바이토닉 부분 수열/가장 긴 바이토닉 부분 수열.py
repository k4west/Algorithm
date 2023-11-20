import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
dp = [[1, 1, 1] for _ in range(N)]
v = {}

for i in range(N):
    a = A[i]
    for j in range(i+1, N):
        if a < A[j] and dp[j][0] < dp[i][0] + 1:
            dp[j][0] = dp[i][0] + 1
        if a > A[j]:
            if dp[j][2] < dp[i][2] + 1:
                dp[j][2] = dp[i][2] + 1
            if dp[j][1] < dp[i][0] + 1:
                dp[j][1] = dp[i][0] + 1
            if dp[j][1] < dp[i][1] + 1:
                dp[j][1] = dp[i][1] + 1

print(max(max(k) for k in dp))