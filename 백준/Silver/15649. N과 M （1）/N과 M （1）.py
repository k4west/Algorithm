def dfs(depth):
    if depth == M:
        ans.append(' '.join(map(str, li)))
        return

    for i in range(1, N+1):
        if visited[i]:
            continue
        li.append(i)
        visited[i] = 1
        dfs(depth+1)
        li.pop()
        visited[i] = 0


ans = []
N, M = map(int, input().split())
visited = [0]*(N+1)
li = []
dfs(0)
print('\n'.join(ans))
