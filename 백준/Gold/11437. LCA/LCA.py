def bfs(s=1):
    q, nq = [s], []
    visited = [0]*(N+1)
    lvl = 0

    visited[s] = 1

    while q or nq:
        if not q:
            q, nq = nq, []
            lvl += 1
        parent = q.pop()
        for child in graph[parent]:
            if visited[child]:
                continue
            
            visited[child] = 1
            roots[child] = parent
            level[child] = lvl+1
            nq.append(child)



def lca(x, y):
    if level[x] < level[y]:
        x, y = y, x
    while level[x] > level[y]:
        x = roots[x]
    while x != y:
        x, y = roots[x], roots[y]
    return x


a = open(0)
N = int(next(a))
roots = [0]*(N+1)
level = [0]*(N+1)
graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    n1, n2 = map(int, next(a).split())
    graph[n1].append(n2)
    graph[n2].append(n1)
bfs()

ans = []
for _ in range(int(next(a))):
    n1, n2 = map(int, next(a).split())
    ans.append(lca(n1, n2))
print('\n'.join(map(str, ans)))
