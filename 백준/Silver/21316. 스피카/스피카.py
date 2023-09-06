import sys
A = [[0]*13 for _ in range(13)]
for _ in range(12):
    a, b = map(int, sys.stdin.readline().split())
    A[a][b], A[b][a] = 1, 1
for i in range(1, 13):
    s = 0
    if sum(A[i]) == 3:
        for j, p in enumerate(A[i]):
            if p:
                s += sum(A[j])
        if s == 6:
            print(i)
            break