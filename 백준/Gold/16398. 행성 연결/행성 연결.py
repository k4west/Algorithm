from heapq import heappop, heappush


def prim(s):
    visited = [0]*(N+1)
    total = cnt = 0

    hq = [(0, s)]
    while hq:
        cw, cur = heappop(hq)
        if visited[cur]:
            continue

        visited[cur] = 1
        total += cw
        cnt += 1

        if cnt == N:
            return total

        for nxt, nw in graph[cur].items():
            if not visited[nxt]:
                heappush(hq, (nw, nxt))


INF = float("inf")
ans = []

N = int(input())
graph = [{} for _ in range(N+1)]
for i in range(N):
    for j, c in enumerate(map(int, input().split())):
        if graph[i].get(j, INF) > c:
            graph[i][j] = c
            graph[j][i] = c

print(prim(1))
