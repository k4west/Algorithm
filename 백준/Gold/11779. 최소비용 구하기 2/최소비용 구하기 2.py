from sys import stdin
from heapq import heappop, heappush

input = stdin.readline

def dijkstra():
    hq = [(0, S)]
    distance[S] = 0

    while hq:
        cc, cur = heappop(hq)
        if cc > distance[cur]:  # 큐에 있는 요금(갱신에 반영할 요금)이 현재 보다 비싸면 무시
            continue
        
        if cur == E:
            break

        for nxt, nc in graph[cur].items():
            c = cc + nc
            if c >= distance[nxt]:   # 비싸면 무시
                continue

            distance[nxt] = c       # 더 저럼하면 반영
            visited[nxt] = cur      # 경로 표시
            heappush(hq, (c, nxt))


INF = float("inf")
n = int(input())
m = int(input())

graph = [{} for _ in range(n+1)]
for _ in range(m):
    s, e, c = map(int, input().split())
    if graph[s].get(e, INF) > c:
        graph[s][e] = c

S, E = map(int, input().split())

distance = [INF]*(n+1)
visited = [0]*(n+1)
dijkstra()

ans = [E]               # 방문 순서를 역으로 추적
while ans[-1] != S:     # 시작 지점을 만날 때까지
    ans.append(visited[ans[-1]])

print(distance[E], len(ans), " ".join(map(str, ans[::-1])), sep='\n')
