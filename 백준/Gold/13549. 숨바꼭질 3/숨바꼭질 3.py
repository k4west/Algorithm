def dfs(n, k):
    if n >= k:
        return n-k
    elif not n:
        return 1 + dfs(n+1, k)
    elif not k % 2:
        return min(k-n, dfs(n, k//2))
    else:
        return 1 + min(dfs(n, k-1), dfs(n, k+1))


N, K = map(int, input().split())
print(dfs(N, K))
