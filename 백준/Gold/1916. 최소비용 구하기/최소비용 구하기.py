from heapq import heappop, heappush


def dijkstra(start):
    # 초기화
    hq = []
    for city, cost in graph[start].items():
        costs[city] = cost
        heappush(hq, (cost, city))

    while hq:
        cost_c, cur = heappop(hq)

        # 더 저렴한 비용이 있다면 반영하기
        for nxt, cost_n in graph[cur].items():
            cost = cost_c + cost_n
            if costs[nxt] > cost:
                costs[nxt] = cost
                heappush(hq, (cost, nxt))


INF = float("INF")
a = open(0)
N = int(next(a))    # 도시의 개수 N(1 ≤ N ≤ 1,000)
M = int(next(a))    # 버스의 개수 M(1 ≤ M ≤ 100,000)

graph = [{} for _ in range(N+1)]    # 도시의 번호: 1 ~ N
costs = [INF]*(N+1)
for _ in range(M):                  # 출발, 도착, 비용; 1 ≤ cost ≤ 100,000
    s, e, c = map(int, next(a).split())
    if graph[s].get(e, INF) > c:
        graph[s][e] = c

S, E = map(int, next(a).split())    # 출발, 도착 -> 최소 비용
costs[S] = 0
dijkstra(S)

print(costs[E])
