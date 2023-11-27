import sys
from heapq import heappop, heappush
input = sys.stdin.readline
# INF = float('inf')

n, m, r = map(int, input().split())
items = [0] + list(map(int, input().split()))
graph = [[] for _ in range(n+1)]

for _ in range(r):
    a, b, l = map(int, input().split())
    graph[a].append((b, l))
    graph[b].append((a, l))

def dijkstra(s):
    dist = [16]*(n+1)
    q = [(0, s)]
    dist[s] = 0
    while q:
        d0, n0 = heappop(q)
        if dist[n0] < d0:
            continue
        for n1, d1 in graph[n0]:
            if (d:=d0+d1) < dist[n1]:
                dist[n1] = d
                heappush(q, (d, n1))
    tmp = 0
    for i, d in enumerate(dist[1:], 1):
        if d <= m:
            tmp += items[i]
    return tmp

ans = 0
for i in range(1, n+1):
    if ans < (tmp:=dijkstra(i)):
        ans = tmp

print(ans)