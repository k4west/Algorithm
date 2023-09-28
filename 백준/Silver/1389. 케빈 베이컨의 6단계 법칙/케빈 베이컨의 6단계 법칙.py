import sys
def f(A, N, i, j):
    li = [A[i][j]]
    for _ in range(N):
        pass
    return min(li)

N, M = map(int, sys.stdin.readline().split())
li = []
for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    li.extend([(i,j), (j,i)])

A = [[0]*(N+1) for _ in range(N+1)]
for i in range(1, N+1):
    for j in range(i, N+1):
        if i == j: continue
        elif (i,j) in li: A[i][j], A[j][i] = 1, 1
        else: A[i][j], A[j][i] = float('inf'), float('inf')

for node in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            if A[i][j] > 1: A[i][j] = min(A[i][j], A[i][node]+A[node][j])

s = [sum(a) for a in A[1:]]

print(s.index(min(s))+1)