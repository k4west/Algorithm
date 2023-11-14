import sys
input = sys.stdin.readline

def main():
    N = int(input())
    graph = [['0']]
    dp = [[[0]*(N+1) for _ in range(N+1)] for _ in range(3)]

    for _ in range(N):
        graph.append(['0']+input().rstrip().split()+['1'])
    graph.append(['1']*(N+2))
    if graph[N][N] == '1' or (graph[N-1][N] == '1' and graph[N][N-1] == '1'):
        print(0)
        exit()

    dp[0][1][2] = 1
    for c in range(3, N+1):
        if graph[1][c] == '0':
            dp[0][1][c] = dp[0][1][c-1]

    for i in range(2, N+1):
        for j in range(3, N+1):
            if graph[i][j] == '0':
                if graph[i-1][j] == graph[i][j-1] == '0':
                    dp[1][i][j] = dp[0][i-1][j-1] + dp[1][i-1][j-1] + dp[2][i-1][j-1]
                dp[0][i][j] = dp[0][i][j-1] + dp[1][i][j-1]
                dp[2][i][j] = dp[2][i-1][j] + dp[1][i-1][j]
    print(dp[0][N][N]+dp[1][N][N]+dp[2][N][N])

if __name__ == "__main__":
    main()