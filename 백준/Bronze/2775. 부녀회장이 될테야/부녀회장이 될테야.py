import sys
T = int(sys.stdin.readline())
for _ in range(T):
    k = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    A = list(range(1,n+1))
    for _ in range(k):
        for i in range(1, n):
            A[i] += A[i-1]
    print(A[n-1])