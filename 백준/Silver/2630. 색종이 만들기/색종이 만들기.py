def g(i, j, N):
    global wb
    c = A[i][j]
    if N == 1: wb[c] += 1; return
    M = N//2
    for s in range(i,i+N):
        for t in range(j,j+N):
            if A[s][t] != c:
                g(i,j,M)
                g(i+M,j,M)
                g(i,j+M,M)
                g(i+M,j+M,M)
                return
    wb[c] += 1
    
import sys
N = int(sys.stdin.readline())
A = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
wb = [0, 0]
g(0, 0, N)
print(*wb, sep='\n')