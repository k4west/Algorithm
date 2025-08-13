from heapq import heappop, heapify


def find(x):
    tmp = []
    while x != roots[x]:
        tmp.append(x)
        x = roots[x]
    
    for px in tmp:
        roots[px] = x

    return x


def union(a, b):
    a = find(a)
    b = find(b)

    if a > b:
        a, b = b, a

    roots[b] = a


N = int(input())
*roots, = range(N)

nodes = []
for i in range(N):
    for j, c in enumerate(map(int, input().split())):
        nodes.append((c, i, j))
heapify(nodes)

total = cnt = 0
while nodes:
    c, i, j = heappop(nodes)

    if find(i) == find(j):
        continue

    union(i, j)
    total += c
    cnt += 1

    if cnt == N-1:
        break

print(total)
