def get_closest_city():
    city = 0
    cost = INF

    # 방문 하지 않은 도시들 중에서 가장 비용이 적은 도시 구하기
    for idx in range(1, N+1):
        if visited[idx]:
            continue

        tmp = costs[idx]
        if cost > tmp:
            city = idx
            cost = tmp

    visited[city] = 1
    return city


def dijkstra(start):
    # 초기화
    for city, cost in graph[start]:
        if costs[city] > cost:
            costs[city] = cost

    # start를 제외한 나머지 노드를 가까운 순서로 탐색
    for _ in range(N-1):
        cur = get_closest_city()
        cost_c = costs[cur]

        # 더 저렴한 비용이 있다면 반영하기
        for nxt, cost_n in graph[cur]:
            cost = cost_c + cost_n
            if costs[nxt] > cost:
                costs[nxt] = cost


INF = float("INF")
N = int(input())    # 도시의 개수 N(1 ≤ N ≤ 1,000)
M = int(input())    # 버스의 개수 M(1 ≤ M ≤ 100,000)

graph = [[] for _ in range(N+1)]    # 도시의 번호: 1 ~ N
costs = [INF]*(N+1)
visited = [0]*(N+1)
for _ in range(M):                  # 출발, 도착, 비용; 1 ≤ cost ≤ 100,000
    s, e, c = map(int, input().split())
    graph[s].append((e, c))

S, E = map(int, input().split())    # 출발, 도착 -> 최소 비용
costs[S] = 0
visited[S] = 1
dijkstra(S)

print(costs[E])
