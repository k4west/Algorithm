import sys
n, m = map(int, sys.stdin.readline().split())
D = [[0]*(m+1) for _ in range(n+1)]
D[0][0] = 1
for i in range(1,n+1):
    for j in range(1,m+1):
        D[i][j] = (D[i-1][j] + D[i-1][j-1] + D[i][j-1])%(10**9+7)
print(D[-1][-1])