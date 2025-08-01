ans = []
INF = float('inf')
for _ in range(int(input())):
    M, N = map(int, input().split())
    graph = [[*map(int, input().split())] for _ in range(N)]

    t = -INF
    idx = -1
    for m in range(M):
        tmp = 1
        for n in range(N):
            tmp *= graph[n][m]

        if t <= tmp:
            t = tmp
            idx = m

    ans.append(idx+1)

print('\n'.join(map(str, ans)))
