import sys
N, M = map(int, sys.stdin.readline().split())
B = [0]*N
for _ in range(M):
    i, j, k = map(int, sys.stdin.readline().split())
    for p in range(i-1,j):
        B[p] = k
print(*B)