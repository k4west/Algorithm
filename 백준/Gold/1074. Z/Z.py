def dfs(a, b):
    if a + b == 0:
        return 0
    return dfs(a//2, b//2)*4 + 2*(a % 2) + (b % 2)


N, r, c = map(int, input().split())
print(dfs(r, c))
