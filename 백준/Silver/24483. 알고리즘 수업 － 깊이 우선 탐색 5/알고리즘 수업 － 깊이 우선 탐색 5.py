import sys
sys.setrecursionlimit(10**9)

N, M, R, *a = map(int, open(0).read().split())
graph = [[] for _ in range(N+1)]
ds = [0 for _ in range(N+1)]
ts = [0 for _ in range(N+1)]
visit = [0 for _ in range(N+1)]

def dfs(node, d, t):
    ds[node] = d
    ts[node] = t
    for next_node in graph[node]:
        if not visit[next_node]:
            visit[next_node] = 1
            t = dfs(next_node, d+1, t+1)
    return t

for i in range(M):
    u, v = a[2*i:2*i+2]
    graph[u].append(v)
    graph[v].append(u)
for i in range(N):
    graph[i+1].sort()
visit[R] = 1
dfs(R, 0, 1)
print(sum([ds[i]*ts[i] for i in range(N+1)]))