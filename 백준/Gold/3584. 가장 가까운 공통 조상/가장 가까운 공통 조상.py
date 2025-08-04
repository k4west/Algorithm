def bfs(r):
    q = [r]
    while q:
        cur = q.pop()
        for nxt in parent[cur]:
            level[nxt] = level[cur]+1
            q.append(nxt)


def lca(x, y):
    if level[x] > level[y]:
        x, y = y, x

    while level[x] != level[y]:
        y = roots[y]

    while x != y:
        x, y = roots[x], roots[y]

    return x


ans = []
T = int(input())
for _ in range(T):
    N = int(input())
    roots = [0]*(N+1)
    level = [0]*(N+1)
    parent = [[] for _ in range(N+1)]

    for _ in range(N-1):
        p, c = map(int, input().split())
        parent[p].append(c)
        roots[c] = p

    for idx in range(1, N+1):
        if not roots[idx]:
            root = idx
            break
    bfs(root)

    ans.append(lca(*map(int, input().split())))

print('\n'.join(map(str, ans)))
