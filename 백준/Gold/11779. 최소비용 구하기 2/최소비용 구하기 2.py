import sys
from heapq import heappop, heappush
input = sys.stdin.readline

INF = float('inf')
n = int(input())
m = int(input())
buses = [{} for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    if c < buses[a].get(b, INF):
        buses[a][b] = c
A, B = map(int, input().split())


dist = [INF]*(n+1)
dist[A] = 0
path = [0]*(n+1)

li = [(0, A)]
while li:
    c0, n0 = heappop(li)
    if c0 > dist[n0]:
        continue
    for n1, c1 in buses[n0].items():
        if (c:=c0+c1) < dist[n1]:
            dist[n1] = c
            path[n1] = n0
            heappush(li, (c, n1))

ans = [B]
while (n:=ans[-1]) != A:
    ans.append(path[n])

print(dist[B], len(ans), sep='\n')
print(*ans[::-1])