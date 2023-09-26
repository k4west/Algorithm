import sys
from collections import deque

def dfs(A, S, v):
    global dfs_li
    v[S] = True
    dfs_li.append(S)
    for a in A[S]:
        if not v[a]:
            dfs(A, a, v)

def bfs(A, S, N):
    li = []
    v = [False] * (N+1)
    q = deque([S])
    v[S] = True
    while q:
        node = q.popleft()
        li.append(node)
        for a in A[node]:
            if not v[a]:
                v[a] = True
                q.append(a)
    print(*li)

if __name__ == "__main__":
    N, M, S = map(int, sys.stdin.readline().split())
    A = [[] for _ in range(N + 1)]

    for _ in range(M):
        i, j = map(int, sys.stdin.readline().split())
        A[i].append(j)
        A[j].append(i)

    for a in A:
        if a:
            a.sort()
    dfs_li = []
    dfs_v = [False] * (N+1)

    dfs(A, S, dfs_v)
    print(*dfs_li)
    bfs(A, S, N)