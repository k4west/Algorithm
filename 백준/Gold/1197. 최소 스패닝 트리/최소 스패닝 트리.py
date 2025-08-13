from heapq import heapify, heappop


def find(x):
    while x != roots[x]:
        x = roots[x]

    return x


def union(a, b):
    a = find(a)
    b = find(b)

    if a > b:
        a, b = b, a

    roots[b] = a


V, E = map(int, input().split())
*roots, = range(V+1)

nodes = []
for _ in range(E):
    A, B, C = map(int, input().split())
    nodes.append((C, A, B))
heapify(nodes)

total = cnt = 0
while cnt < V-1:
    c, a, b = heappop(nodes)

    if find(a) == find(b):
        continue

    union(a, b)
    total += c
    cnt += 1

print(total)
