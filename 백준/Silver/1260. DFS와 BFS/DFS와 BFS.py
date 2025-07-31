def dfs(s):
    ans = [s]
    stack = []
    visited = [0]*(N+1)

    visited[s] = 1

    while True:
        for n in graph[s]:
            if not visited[n]:
                visited[n] = 1
                stack.append(s)
                ans.append(n)
                s = n
                break
        else:
            if stack:
                s = stack.pop()
            else:
                return ' '.join(map(str, ans))


def bfs(s):
    ans = [s]
    q = [s]
    visited = [0]*(N+1)

    visited[s] = 1
    while q:
        s = q.pop(0)
        for n in graph[s]:
            if not visited[n]:
                visited[n] = 1
                q.append(n)
                ans.append(n)
    return ' '.join(map(str, ans))


N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)
    
for n in range(1, N+1):
    graph[n].sort()
    
print(dfs(V))
print(bfs(V))