from heapq import heappop, heappush


def dijkstra_min(s, arr):
    cnts = [INF] * (N + 1)
    costs = [INF] * (N + 1)
    cnts[s] = 0
    costs[s] = 0

    pq = [(0, 0, s)]

    while pq:
        cnt, cost, cur = heappop(pq)
        if cnt != cnts[cur] or cost != costs[cur]:
            continue
        for nxt, ncost in arr[cur]:
            ncnt = cnt + 1
            ncost += cost + T[nxt]
            if ncnt < cnts[nxt] or ncnt == cnts[nxt] and ncost < costs[nxt]:
                cnts[nxt] = ncnt
                costs[nxt] = ncost
                heappush(pq, (ncnt, ncost, nxt))

    return cnts, costs


def dijkstra_max(s, arr):
    cnts = [INF] * (N + 1)
    costs = [-1] * (N + 1)
    cnts[s] = 0
    costs[s] = 0

    pq = [(0, 0, s)]

    while pq:
        cnt, cost, cur = heappop(pq)
        cost *= -1
        if cnt != cnts[cur] or cost != costs[cur]:
            continue
        for nxt, ncost in arr[cur]:
            ncnt = cnt + 1
            ncost += cost + T[nxt]
            if ncnt < cnts[nxt] or ncnt == cnts[nxt] and ncost > costs[nxt]:
                cnts[nxt] = ncnt
                costs[nxt] = ncost
                heappush(pq, (ncnt, -ncost, nxt))

    return cnts, costs


INF = float("inf")
N, M = map(int, input().split())
T = [0, 0] + [*map(int, input().split())]
graph = [[] for _ in range(N + 1)]
rgraph = [[] for _ in range(N + 1)]

for _ in range(M):
    v, w, F = map(int, input().split())
    graph[v].append((w, F))
    rgraph[w].append((v, F))

f_min_cnt, t_min_cost = dijkstra_min(1, graph)
rf_min_cnt, rt_min_cost = dijkstra_min(1, rgraph)

f_max_cnt, t_max_cost = dijkstra_max(1, graph)
rf_max_cnt, rt_max_cost = dijkstra_max(1, rgraph)

min_flight = min((f+rf for f, rf in zip(f_min_cnt[2:], rf_min_cnt[2:])))

min_ans = INF
max_ans = 0
for city in range(2, N+1):
    if f_min_cnt[city] + rf_min_cnt[city] == min_flight:
        if min_ans > t_min_cost[city] + rt_min_cost[city] - T[city]:
            min_ans = t_min_cost[city] + rt_min_cost[city] - T[city]
        if max_ans < t_max_cost[city] + rt_max_cost[city] - T[city]:
            max_ans = t_max_cost[city] + rt_max_cost[city] - T[city]

print(min_ans)
print(max_ans)
