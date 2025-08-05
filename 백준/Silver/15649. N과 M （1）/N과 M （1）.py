def dfs(depth):
    if depth == M:
        ans.append(' '.join(map(str, li)))
        return

    for i in range(1, N+1):
        if not i in li:
            li.append(i)
            dfs(depth+1)
            li.pop()


ans = []
N, M = map(int, input().split())
li = []
dfs(0)
print('\n'.join(ans))
