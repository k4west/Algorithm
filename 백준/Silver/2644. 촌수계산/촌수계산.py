def dfs(n):
    stack = []
    dist = 0
    visited[n] = 1
    while True:
        for nn in graph[n]:
            if nn == G:
                return dist + 1
            if not visited[nn]:
                dist += 1
                visited[nn] = 1
                stack.append(n)
                n = nn
                break
        else:
            if stack:
                n = stack.pop()
                dist -= 1
            else:
                return 0

n = int(input())
graph = [[] for _ in range(n+1)]
visited = [0]*(n+1)

S, G = map(int, input().split())
m = int(input())
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

print(dfs(S) or -1)
