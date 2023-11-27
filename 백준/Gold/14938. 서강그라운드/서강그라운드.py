import sys
input = sys.stdin.readline
INF = float('inf')

n, m, r = map(int, input().split())
items = [0] + list(map(int, input().split()))
graph = [[INF]*(n+1) for _ in range(n+1)]

for _ in range(r):
    a, b, l = map(int, input().split())
    graph[a][b] = l
    graph[b][a] = l
    
for node in range(1, n+1):
    graph[node][node] = 0
    for i in range(1, n+1):
        for j in range(i+1, n+1):
            if graph[i][j] > graph[i][node] + graph[node][j]:
                graph[i][j] = graph[i][node] + graph[node][j]
                graph[j][i] = graph[i][j]

ans = 0
for i in range(1, n+1):
    tmp = 0
    for j in range(1, n+1):
        if graph[i][j] <= m:
            tmp += items[j]
    if ans < tmp:
        ans = tmp

print(ans)