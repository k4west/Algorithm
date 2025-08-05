def dfs(i, s, f):
    global ans

    if i == N:
        ans += f and s == S
        return

    dfs(i+1, s, f | 0)
    dfs(i+1, s+li[i], 1)


ans = 0
N, S, *li = map(int, open(0).read().split())
dfs(0, 0, 0)
print(ans)