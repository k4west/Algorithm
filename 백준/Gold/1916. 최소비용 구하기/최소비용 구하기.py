from sys import stdin
from heapq import heappush, heappop
input = stdin.readline
INF = float('INF')

def dijkstra(graph, s, e, N):
    costs = [INF]*(N+1)
    q = []
    heappush(q, (0, s))
    costs[s] = 0
    while q:
        s_cost, node = heappop(q)
        if costs[node] < s_cost: continue
        if node == e: break
        for dst, d_cost in graph[node].items():
            d_cost += costs[node]
            if d_cost < costs[dst]:
                costs[dst] = d_cost
                heappush(q, (d_cost, dst))
    print(costs[e])

def main():
    N = int(input())
    M = int(input())
    graph = [{} for _ in range(N+1)]
    for _ in range(M):
        s, e, c = map(int, input().split())
        if e in graph[s]:
            graph[s][e] = min(graph[s][e], c)
        else:
            graph[s][e] = c
    s, e = map(int, input().split())
    dijkstra(graph, s, e, N)

if __name__ == "__main__":
    main()