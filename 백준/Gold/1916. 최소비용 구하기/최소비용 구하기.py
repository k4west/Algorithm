from sys import stdin
from heapq import heappush, heappop
input = stdin.readline
INF = float('INF')

def main():
    N = int(input())
    M = int(input())

    graph = [[] for _ in range(N+1)]
    costs = [INF]*(N+1)

    for _ in range(M):
        s, e, c = map(int, input().split())
        graph[s].append((e, c))

    def dijkstra(s, e):
        q = []
        heappush(q, (0, s))
        costs[s] = 0
        while q:
            s_cost, node = heappop(q)
            if costs[node] < s_cost: continue
            if node == e: break
            for dst, d_cost in graph[node]:
                d_cost += costs[node]
                if d_cost < costs[dst]:
                    costs[dst] = d_cost
                    heappush(q, (d_cost, dst))

        print(costs[e])

    s, e = map(int, input().split())
    dijkstra(s, e)

if __name__ == "__main__":
    main()