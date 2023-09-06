import sys
A = [[0]*13 for _ in range(13)]
for _ in range(12):
    a, b = map(int, sys.stdin.readline().split())
    A[a][b], A[b][a] = 1, 1

li = []
for i in range(1, 13):
    if sum(A[i]) == 3:
        li.append(i)

for p in li:
    s = 0
    for i, q in enumerate(A[p]):
        if q:
            s += sum(A[i])
    if s == 6:
        print(p)