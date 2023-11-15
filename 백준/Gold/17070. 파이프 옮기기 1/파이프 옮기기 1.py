import sys
input = sys.stdin.readline

N = int(input())
graph = [['0']]
dp = [[[0, 0, 0] for _ in range(N+1)] for _ in range(N+1)]

for _ in range(N):
    graph.append(['0']+input().rstrip().split()+['1'])
graph.append(['1']*(N+2))
if graph[N][N] == '1' or (graph[N-1][N] == '1' and graph[N][N-1] == '1'):
    print(0)
    exit()

dp[1][2][0] = 1
for c in range(3, N+1):
    if graph[1][c] == '0':
        dp[1][c][0] = dp[1][c-1][0]

for i in range(2, N+1):
    for j in range(3, N+1):
        if graph[i][j] == '0':
            if graph[i-1][j] == graph[i][j-1] == '0':
                dp[i][j][1] = sum(dp[i-1][j-1])
            dp[i][j][0] = dp[i][j-1][0] + dp[i][j-1][1]
            dp[i][j][2] = dp[i-1][j][2] + dp[i-1][j][1]
print(sum(dp[N][N]))