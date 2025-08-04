N = int(input())

graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

trees = [0]*(N+1)
trees[1] = -1
q = [1]
while q:
    parent = q.pop()
    for child in graph[parent]:
        if not trees[child]:
            trees[child] = parent
            q.append(child)

print('\n'.join(map(str, trees[2:])))
