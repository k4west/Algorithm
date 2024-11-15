import sys

def dfs(S):
    v[S] = True
    li.append(S)
    for a in A[S]:
        if not v[a]:
            dfs(a)

def bfs(S):
    v[S] = True
    q = [S]
    while q:
        node = q.pop(0)
        li.append(node)
        for a in A[node]:
            if not v[a]:
                v[a] = True
                q.append(a)

N, M, S = map(int, sys.stdin.readline().split())
A = [[] for _ in range(N + 1)]

for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    A[i].append(j)
    A[j].append(i)

for a in A:
    if a:
        a.sort()
        
li = []
v = [False] * (N+1)
dfs(S)
print(" ".join(map(str, li)))

li = []
v = [False] * (N+1)
bfs(S)
print(" ".join(map(str, li)))