from heapq import heappop, heapify


def lan_len(lan):
    if lan == "0":
        return 0

    if ord(lan) > 96:
        return ord(lan) - 96
    return ord(lan)-38


def find(x):
    if x != root[x]:
        root[x] = find(root[x])
    return root[x]


def union(a, b):
    a = find(a)
    b = find(b)

    root[b] = a


total = min_lan = cnt = 0
N = int(input())
*root, = range(N)

nodes = []
for i in range(N):
    for j, c in enumerate(map(lan_len, input())):
        total += c
        if i != j and c:
            nodes.append((c, i, j))
heapify(nodes)

while nodes:
    c, i, j = heappop(nodes)
    if find(i) == find(j):
        continue

    union(i,  j)
    min_lan += c
    cnt += 1

    if cnt == N-1:
        break

if cnt == N-1:
    print(total - min_lan)
else:
    print(-1)
    