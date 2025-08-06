def f(i, s):
    global ans

    if i == N:
        t = sum(abs(s[k]-s[k+1]) for k in range(N-1))
        if ans < t:
            ans = t
        return

    for j in range(N):
        if not visited[j]:
            visited[j] = 1
            f(i+1, s+[li[j]])
            visited[j] = 0


ans = 0
N = int(input())
*li, = map(int, input().split())
visited = [0]*N
f(0, [])
print(ans)