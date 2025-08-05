def dfs(s=1):
    visited[1] = 1
    dp[1][1] = 1

    stack = []
    while True:
        for e in graph[s]:
            if not visited[e]:
                visited[e] = 1
                dp[e][1] = 1
                stack.append((s, e))
                s = e
                break
        else:
            if stack:
                s, p = stack.pop()
                dp[s][0] += dp[p][1]
                dp[s][1] += min(dp[p])
            else:
                break


N = int(input())
graph = [[] for _ in range(N+1)]
visited = [0]*(N+1)
dp = [[0, 0] for _ in range(N+1)]

for _ in range(N-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

dfs()
print(min(dp[1]))