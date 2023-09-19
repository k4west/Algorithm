import sys

def f(i, v, A):
    li = [i]
    v[i] = True
    while li:
        j = li.pop(0)
        for k in A[j]:
            if not v[k]:
                li.append(k)
                v[k] = True

N, M = map(int, sys.stdin.readline().split())
A = [[] for _ in range(N+1)]
for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    A[i].append(j)
    A[j].append(i)
    
c = 0
v = [False] * (N+1)
for i in range(1,N+1):
    if not v[i]:
        f(i, v, A)
        c += 1
print(c)