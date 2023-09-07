import sys
T = int(sys.stdin.readline())
for _ in range(T):
    k = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    A = [list(range(1,n+1)) for _ in range(k+1)]
    for i in range(1, k+1):
        for j in range(1, n):
            A[i][j] = A[i][j-1] + A[i-1][j]
    print(A[k][n-1])