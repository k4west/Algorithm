import sys
from heapq import heappop, heappush
input = sys.stdin.readline

def main():
    INF = float('inf')
    N, E = map(int, input().split())
    graph = [[] for _ in range(N+1)]

    for _ in range(E):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
        graph[b].append((a, c))

    v1, v2 = map(int, input().split())

    def f(node, li):
        dist = [INF]*(N+1)
        dist[node] = 0
        q = [(0, node)]
        while q:
            d0, s = heappop(q)
            for e, d1 in graph[s]:
                if (d:= d0 + d1) < dist[e]:
                    dist[e] = d
                    heappush(q, (d, e))
        return [dist[i] for i in li]
    
    d1, d2 = f(v1, [1, N, v2]), f(v2, [N, 1])
    ans = min([x+y for x, y in zip(d1, d2)]) + d1[2]
    print(ans if ans != INF else '-1')

if __name__ == "__main__":
    main()