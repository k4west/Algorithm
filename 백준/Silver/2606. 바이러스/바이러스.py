def dfs(c):
    for nc in graph[c]:        # 인접한 컴퓨터에 대해서
        if not visited[nc]:
            visited[nc] = 1    # 방문 기록
            dfs(nc)            # 인접 컴퓨터의 인접 컴퓨터 탐색


C = int(input())
graph = [[] for _ in range(C+1)]
visited = [0]*(C+1)
visited[1] = 1
for _ in range(int(input())):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)
dfs(1)
print(sum(visited)-1)        # (1번 컴퓨터, 방문한 컴퓨터) = 감염된 컴퓨터