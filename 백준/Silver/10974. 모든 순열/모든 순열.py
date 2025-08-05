def dfs(depth):
    if depth == N:
        ans.append(' '.join(map(str, li)))
        return

    for n in range(1, N+1):
        if visited[n]:
            continue
        visited[n] = 1
        li.append(n)
        dfs(depth+1)
        li.pop()
        visited[n] = 0

        
ans = []
N = int(input())
visited = [0]*(N+1)
li = []
dfs(0)
print('\n'.join(ans))
