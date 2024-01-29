import sys
from heapq import heappop, heappush

input = lambda: map(int, sys.stdin.readline().split())
N, M = input()
graph, degs = [[] for _ in range(N + 1)], [0 for _ in range(N + 1)]
v = set(range(1, 1 + N))

for _ in range(M):
    a, b = input()
    graph[a].append(b)
    degs[b] += 1
    v.discard(b)

heap, ans = list(v), []

while heap:
    a = heappop(heap)
    ans.append(str(a))
    for b in graph[a]:
        degs[b] -= 1
        if not degs[b]:
            heappush(heap, b)

print(" ".join(ans))