N, *li = map(int, open(0).read().split())

graph = [[] for _ in range(N+1)]
for i in range(N-1):
    a, b = li[2*i:2*i+2]
    graph[a].append(b)
    graph[b].append(a)

trees = [0]*(N+1)
trees[1] = -1
s = [1]
while s:
    parent = s.pop()
    for child in graph[parent]:
        if not trees[child]:
            trees[child] = parent
            s.append(child)

print('\n'.join(map(str, trees[2:])))
