def dfs(s, e):
    visited[s] = 1

    for m, w in trees[s]:
        if m == e:
            return w
        
        if not visited[m]:
            t = dfs(m, e)
            if t:
              return t + w
    return 0


ans = []
N, M = map(int, input().split())
trees = [[] for _ in range(N+1)]

for _ in range(N-1):
    s, e, w = map(int, input().split())
    trees[s].append((e, w))
    trees[e].append((s, w))
 
for _ in range(M):
    s, e = map(int, input().split())
    visited = [0]*(N+1)
    ans.append(dfs(s, e))

print('\n'.join(map(str, ans)))