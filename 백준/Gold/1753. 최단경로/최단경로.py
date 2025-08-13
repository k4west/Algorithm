from heapq import heappop, heappush


def dijkstra(s):
    visited = [0]*(V+1)

    hq = [(0, s)]
    distance[s] = 0
    visited[s] = 1

    while hq:
        dist_c, cur = heappop(hq)
        if distance[cur] != dist_c:
            continue

        for nxt, dist_n in graph[cur].items():
            dist = dist_c + dist_n
            if distance[nxt] > dist:
                distance[nxt] = dist
                heappush(hq, (dist, nxt))


# 시작점에서 다른 모든 정점으로의 최단 경로
INF = float("inf")
V, E = map(int, input().split())    # (1 ≤ V ≤ 20,000, 1 ≤ E ≤ 300,000)
K = int(input())                    # 시작점

distance = [INF]*(V+1)              # 1부터 V까지
graph = [{} for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    if graph[u].get(v, INF) > w:    #  여러 개의 간선이 존재할 수도 있음
        graph[u][v] = w

dijkstra(K)

print("\n".join(map(str, distance[1:])).upper())
