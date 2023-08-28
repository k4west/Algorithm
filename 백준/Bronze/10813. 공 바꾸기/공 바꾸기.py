import sys
N, M = map(int, sys.stdin.readline().split())
B = [i+1 for i in range(N)]
for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    B[i-1], B[j-1] = B[j-1], B[i-1]
print(*B)