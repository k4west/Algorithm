import sys
n, m = map(int, sys.stdin.readline().split())
D = [[0]*m for _ in range(n)]

for i in range(n):
    D[i][0] = 1

for j in range(m):
    D[0][j] = 1
    
for i in range(1,n):
    for j in range(1,m):
        D[i][j] = (D[i-1][j] + D[i-1][j-1] + D[i][j-1])%(1000000007)

print(D[n-1][m-1])