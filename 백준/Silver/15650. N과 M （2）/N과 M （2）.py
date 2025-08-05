def dfs(depth):
    if depth == M:
        print(' '.join(map(str, li)))
        return

    s = li[-1]+1 if depth else 1
    for i in range(s, N+1):
        li.append(i)
        dfs(depth+1)
        li.pop()


N, M = map(int, open(0).read().split())
li = []
dfs(0)