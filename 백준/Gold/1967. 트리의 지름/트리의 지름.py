import sys
input = sys.stdin.readline
n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    p, c, w = map(int, input().split())
    graph[p].append((c, w))
    graph[c].append((p, w))

def dfs(n):
    distance, s = 0, 1
    v = set()
    stack = [(n, 0)]
    while stack:
        n, d = stack.pop()
        v.add(n)
        for node, weight in graph[n]:
            if node in v:
                continue
            n_d = d + weight
            if n_d >= distance:
                distance = n_d
                s = node
            v.add(node)
            stack.append((node, n_d))
    return (s, distance)

print(dfs(dfs(1)[0])[1])