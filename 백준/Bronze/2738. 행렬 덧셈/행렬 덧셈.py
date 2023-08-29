import sys
N, M = map(int, sys.stdin.readline().split())
A = [[0]*M for _ in range(N)]
for i in range(2*N):
    temp = map(int, sys.stdin.readline().split())
    for j, k in enumerate(temp):
        A[i%N][j] += k
for a in A:
    print(*a)