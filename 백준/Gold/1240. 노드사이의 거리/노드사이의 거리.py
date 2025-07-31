def bfs(s=1):
    q, nq = [s], []
    visited = [0] * (N + 1)
    roots[s] = (0, 0)
    lvl = 0

    visited[s] = 1

    while q or nq:
        if not q:
            q, nq = nq, []
            lvl += 1
        parent = q.pop()
        for child, w in graph[parent]:
            if visited[child]:
                continue

            visited[child] = 1
            roots[child] = (parent, w)
            level[child] = lvl + 1
            nq.append(child)


def lca(x, y):
    dist = 0
    i, j = x, y
    if i > j:
        i, j = j, i
    if (i, j) in record:
        return record[(i, j)]
    if level[x] < level[y]:
        x, y = y, x
    while level[x] > level[y]:
        x, xw = roots[x]
        dist += xw
    while x != y:
        x, xw = roots[x]
        y, yw = roots[y]
        dist += xw + yw
    record[i, j] = dist
    return dist


a = open(0)
N, M = map(int, next(a).split())
roots = [0] * (N + 1)
level = [0] * (N + 1)
graph = [[] for _ in range(N + 1)]
record = {}

for _ in range(N - 1):
    n1, n2, w = map(int, next(a).split())
    graph[n1].append((n2, w))
    graph[n2].append((n1, w))
bfs()

ans = []
for _ in range(M):
    n1, n2 = map(int, next(a).split())
    ans.append(lca(n1, n2))
print('\n'.join(map(str, ans)))
