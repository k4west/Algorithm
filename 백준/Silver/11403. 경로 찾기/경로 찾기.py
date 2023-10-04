import sys
INF = float('inf')
N = int(sys.stdin.readline())
graph = [[INF]*N for _ in range(N)]
for i in range(N):
    for j, k in enumerate(sys.stdin.readline().rstrip().split()):
        if k == "1":
            graph[i][j] = 1

for node in range(N):
    for i in range(N):
        for j in range(N):
            graph[i][j] = min(graph[i][j], graph[i][node]+graph[node][j])

answer = [['1']*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if graph[i][j] == INF:
            answer[i][j] = '0'

print("\n".join(" ".join(row) for row in answer))