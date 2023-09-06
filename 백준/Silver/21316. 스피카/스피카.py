import sys
def f(A):
    for _ in range(12):
        a, b = map(int, sys.stdin.readline().split())
        A[a].append(b)
        A[b].append(a)
        
    li = []
    for i in range(1, 13):
        if len(A[i]) == 3:
            li.append(i)

    for p in li:
        s = 0
        for i in A[p]:
            s += len(A[i])
        if s == 6:
            return p
A = [[] for _ in range(13)]
print(f(A))