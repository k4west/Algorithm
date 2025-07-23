paint = [[0]*100 for _ in range(100)]
N, M = map(int, input().split())
for _ in range(N):
    x0, y0, x1, y1 = map(int, input().split())
    for x in range(x0-1, x1):
        for y in range(y0-1, y1):
            paint[x][y] += 1
print(sum(1 for i in range(100) for j in range(100) if paint[i][j] > M))
