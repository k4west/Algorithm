from heapq import heappop, heappush


def prim(s):
    visited = [0]*(N+1)
    cnt = 0

    hq = [(-201, s, s)]
    path[s] = [s, -1]
    while hq:
        cw, prev, cur = heappop(hq)
        if visited[cur]:
            continue

        visited[cur] = 1
        width[prev][cur] = -cw
        width[cur][prev] = -cw
        level = path[prev][1]
        path[cur] = (prev, level+1)
        cnt += 1

        if cnt == N:
            break

        for nxt, nw in graph[cur].items():
            if not visited[nxt]:
                heappush(hq, (nw, cur, nxt))


def lca(i, j):
    max_w = 200

    if path[i][1] > path[j][1]:
        i, j = j, i

    while path[i][1] != path[j][1]:
        nj = path[j][0]
        tmp_w = width[j][nj]

        if max_w > tmp_w:
            max_w = tmp_w

        j = nj

    while i != j:
        ni, nj = path[i][0], path[j][0]
        for tmp_w in (width[i][ni], width[j][nj]):
            if max_w > tmp_w:
                max_w = tmp_w

        i, j = ni, nj

    return max_w


ans = []
a = open(0)
# 도시의 수 N, 운하의 수 M, 노선의 수 K (N ≤ 1000, M ≤ 100000, K ≤ 10000)
N, M, K = map(int, next(a).split())

graph = [{} for _ in range(N+1)]
for _ in range(M):
    i, j, w = map(int, next(a).split())     # i와 j 사이에 폭이 w인 운하 (1 ≤ i, j ≤ N, w ≤ 200)
    if graph[i].get(j, 0) > -w:          # 경로는 여러 개가 존재할 수 있다
        graph[i][j] = -w
        graph[j][i] = -w


width = [[0]*(N+1) for _ in range(N+1)]
*path, = range(N+1)
prim(1)

for _ in range(K):
    i, j = map(int, next(a).split())        # 연결하는 도시 i, j
    ans.append(lca(i, j))

print("\n".join(map(str, ans)))
