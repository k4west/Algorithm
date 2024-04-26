def f(i, j):
    q = [(i, j)]
    nq = []
    flag = False
    while q:
        for i, j in q:
            for di, dj in d:
                if 1 <= (ni:=i+di) < n-1 and 1 <= (nj:=j+dj) < m-1 and graph[ni][nj] != 'X':
                    nq.append((ni, nj))
                    if not flag and graph[ni][nj] == '.': flag = True
                    graph[ni][nj] = 'X'
        q, nq = nq, []
    return flag

n, m = map(int, input().split())
d = ((0, 1), (1, 0), (0, -1), (-1, 0))
graph = [list(input()) for _ in range(n)]
i = s = t = 0
j = -1
for di, dj in d:
    while 0 <= (ni:=i+di) < n and 0 <= (nj:=j+dj) < m:
        i, j = ni, nj
        if graph[ni][nj] != 'X' and f(ni, nj): s += 1
for i in range(1, n-1):
    for j in range(1, m-1):
        if graph[i][j] == '.': t += 1
print(s, t)