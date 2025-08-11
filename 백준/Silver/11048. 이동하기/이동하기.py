N, M = map(int, input().split())
maze = [[0]*(M+1)] + [[0] + [*map(int, input().split())] for _ in range(N)]

for r in range(1, N+1):
    for c in range(1, M+1):
        maze[r][c] += max(maze[r][c-1], maze[r-1][c])

print(maze[N][M])