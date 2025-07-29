def bfs(n):
    q, nq = [n], []
    while q or nq:
        if not q:
            q, nq = nq, []
        for node in graph[q.pop()]:
            if not visited[node]:
                visited[node] = 1
                nq.append(node)


C = int(input())
graph = [[] for _ in range(C+1)]
visited = [0] * (C+1)
for _ in range(int(input())):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
visited[1] = 1
bfs(1)
print(sum(visited)-1)
