from sys import stdin
n = int(stdin.readline())
graph = []
for _ in range(n):
    graph.append(list(map(int, stdin.readline().split())))

for i, row in enumerate(graph[1:]):
    graph[i+1][0] += graph[i][0]
    graph[i+1][i+1] += graph[i][i]
    
    for j in range(1, i+1):
        graph[i+1][j] += max(graph[i][j-1], graph[i][j])

print(max(graph[n-1]))