M = 10**9+7
dx = (0, 0, -1, 1)
dy = (-1, 1, 0, 0)

def mat(A, B):
    return [[sum(i*j%M for i, j in zip(r, c))%M for c in zip(*B)] for r in A]

def bimat(A, k):
    if k == 1:
        return A
    T = bimat(A, k//2)
    if k%2:
        return mat(mat(T,T),A)
    else:
        return mat(T,T)
    
def solution(grid, d, k):
    n, m, c = len(grid), len(grid[0]), len(d)
    dp = [[[0]*n*m for _ in range(n*m)] for _ in range(c+1)]
    for i in range(n*m):
        dp[0][i][i] = 1
    
    for t in range(1, c+1):
        diff = d[t-1]
        tmp = dp[t-1]
        for i in range(n):
            for j in range(m):
                h = grid[i][j]
                for di, dj in zip(dx, dy):
                    if 0 <= (ni:=i+di) < n and 0 <= (nj:=j+dj) < m and grid[ni][nj]==h+diff:
                        for s in range(n*m):
                            dp[t][s][m*ni+nj] = (dp[t][s][m*ni+nj] + tmp[s][m*i+j])%M
    
    A = bimat(dp[c],k)
    s = 0
    for row in A:
        for c in row:
            s += c
            s %= M

    return s