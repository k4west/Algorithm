def dfs(s, f):
    if s == N:
        k[1] += f and k[0] == S
        return
    t = li[s]
    dfs(s+1, f | 0)
    k[0] += t
    dfs(s+1, 1)
    k[0] -= t


N, S, *li = map(int, open(0).read().split())
k = [0, 0]
dfs(0, 0)
print(k[1])
