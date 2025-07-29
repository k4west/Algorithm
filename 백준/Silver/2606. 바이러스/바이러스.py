def dfs(c):
    for nc in graph[c]:
        if not visited[nc]:
            visited[nc] = 1
            dfs(nc)


C = int(input())
graph = [[] for _ in range(C+1)]
visited = [0]*(C+1)
visited[1] = 1
for _ in range(int(input())):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)
dfs(1)
print(sum(visited)-1)