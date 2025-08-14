from heapq import heappop, heappush


def dijkstra():
    times = [INF]*N

    hq = [(0, 0)]
    times[0] = 0
    visited[0] = 1

    while hq:
        ct, cur = heappop(hq)
        if ct > times[cur]:
            continue

        for nxt, nt in graph[cur]:
            tt = ct + nt

            if times[nxt] > tt:
                times[nxt] = tt
                heappush(hq, (tt, nxt))

    if times[N-1] != INF:
        return times[N-1]
    return -1


INF = float("inf")
N, M = map(int, input().split())    # 노드, 엣지 느낌
*visited, = map(int, input().split())   # 시야에 보이면 방문 안할 거라 방문한 걸로 표시
visited[N-1] = 0                        # 마지막에 방문 해야 해서;;

graph = [[] for _ in range(N)]
for _ in range(M):
    a, b, t = map(int, input().split())     # 양방향, 같은 경로 중복x
    if not visited[a] and not visited[b]:
        graph[a].append((b, t))
        graph[b].append((a, t))

print(dijkstra())
