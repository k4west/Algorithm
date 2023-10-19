from sys import stdin
n = int(stdin.readline())
graph = [int(stdin.readline())]

for i in range(n-1):
    new = list(map(int, stdin.readline().split()))
    graph = [new[0] + graph[0], *[new[j] + max(graph[j-1], graph[j]) for j in range(1, i+1)], new[i+1] + graph[i]]

print(max(graph))