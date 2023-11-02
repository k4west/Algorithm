import sys
from heapq import heappop, heappush

def main():
    input = sys.stdin.readline

    INF = float('inf')
    N, M, X = map(int, input().split())
    graph1 = [[] for _ in range(N+1)]
    graph2 = [[] for _ in range(N+1)]
    ans = 0
    for _ in range(M):
        s, e, w = map(int, input().split())
        graph1[s].append((e, w))
        graph2[e].append((s, w))

    def dijkstra(X, graph):
        dist = [INF] * (N+1)
        dist[X] = 0
        q = [(0, X)]
        while q:
            w0, n0 = heappop(q)
            if w0 > dist[n0]:
                continue
            for n1, w1 in graph[n0]:
                w = w0 + w1
                if w < dist[n1]:
                    dist[n1] = w
                    heappush(q, (w, n1))
        return dist[1:]

    for i, j in zip(dijkstra(X, graph1), dijkstra(X, graph2)):
        if ans < i + j:
            ans = i + j
    print(ans)

if __name__ == "__main__":
    main()