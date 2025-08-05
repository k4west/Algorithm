def dfs(s, k):
    global cnt

    if s and k == S:
        cnt += 1

    for i in range(s, N):
        dfs(i+1, k+li[i])


cnt = 0
N, S, *li = map(int, open(0).read().split())
dfs(0, 0)
print(cnt)
