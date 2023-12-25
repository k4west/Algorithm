import sys
input = sys.stdin.readline

INF = float('inf')
d = [[2, 2, 2, 2, 2],
     [0, 1, 3, 4, 3],
     [0, 3, 1, 3, 4],
     [0, 4, 3, 1, 3],
     [0, 3, 4, 3, 1]]

arr = list(map(int, input()[:-2].split()))
n = len(arr)
dp = [[[INF]*5 for _ in range(5)] for _ in range(n+1)]
dp[-1][0][0] = 0 

for i in range(n):
    a = arr[i]
    for j in range(5):
        for k in range(5):
            dp[i][a][j] = min(dp[i][a][j], dp[i-1][k][j] + d[k][a])
    
    for j in range(5):
        for k in range(5):
            dp[i][j][a] = min(dp[i][j][a], dp[i-1][j][k] + d[k][a])

ans = INF
for i in range(5):
    for j in range(5):
        if ans > (tmp:=dp[n-1][i][j]):
            ans = tmp
print(ans)