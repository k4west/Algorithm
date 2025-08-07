def dfs(n):
    global cnt

    if n == N:
        cnt += 1
        return

    for i in range(N):
        if v1[i] == 0 and v2[n+i] == 0 and v3[n-i] == 0:
            v1[i] = v2[n+i] = v3[n-i] = 1
            dfs(n+1)
            v1[i] = v2[n+i] = v3[n-i] = 0


cnt = 0
N = int(input())
v1 = [0]*N
v2 = [0]*2*N
v3 = [0]*2*N
dfs(0)
print(cnt)