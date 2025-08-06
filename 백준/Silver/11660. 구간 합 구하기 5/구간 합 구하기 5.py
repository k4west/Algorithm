ans = []
N, M = map(int, input().split())
arr = [[*map(int, input().split())] for _ in range(N)]

acc = [[0]*(N+1) for _ in range(N+1)]
for i in range(N):
    for j in range(N):
        acc[i][j] = acc[i][j-1] + arr[i][j]
    for j in range(N):
        acc[i][j] += acc[i-1][j]

for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    ans.append(acc[x1-2][y1-2] + acc[x2-1][y2-1] - acc[x1-2][y2-1] - acc[x2-1][y1-2])

print('\n'.join(map(str, ans)))