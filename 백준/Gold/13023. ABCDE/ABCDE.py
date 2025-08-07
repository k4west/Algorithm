def dfs(cur, cnt):
    global ans
    
    if cnt == 4:
        ans = 1
        return
    
    for nxt in graph[cur]:
        if not visited[nxt]:
            visited[nxt] = 1
            dfs(nxt, cnt+1)
            visited[nxt] = 0


ans = 0
N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [0]*(N+1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for start in range(1, N+1):
    visited[start] = 1
    dfs(start, 0)
    if ans:
        break
    visited[start] = 0

print(ans)