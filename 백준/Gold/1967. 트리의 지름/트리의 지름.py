import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n = int(input())
graph = [[] for _ in range(n+1)]
tmp, last = set(), set()
for _ in range(n-1):
    p, c, w = map(int, input().split())
    graph[p].append((c, w))
    graph[c].append((p, w))
    tmp.add(p)
    last.add(c)
last -= tmp

def dfs(n, d, v):
    global distance
    global s
    for node, weight in graph[n]:
        if node in v:
            continue
        n_d = d + weight
        if node in last:
            if n_d >= distance:
                distance = n_d
                s = node
        else:
            v.add(node)
            dfs(node, n_d, v)
distance, s = 0, 1
dfs(1, 0, {1})
dfs(s, 0, {s})
print(distance)