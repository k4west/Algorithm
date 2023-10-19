from sys import stdin
n = int(stdin.readline())
graph = [int(stdin.readline())]

for i in range(n-1):
    new = list(map(int, stdin.readline().split()))
    new[0] += graph[0]
    new[i+1] += graph[i]
    
    for j in range(1, i+1):
        new[j] += max(graph[j-1], graph[j])
    
    graph = new

print(max(graph))