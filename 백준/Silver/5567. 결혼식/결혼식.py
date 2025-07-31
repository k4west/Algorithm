N = int(input())
graph = [[] for _ in range(N+1)]
visited = [0]*(N+1)

for _ in range(int(input())):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

q, nq = [1], []
visited[1] = 1
cnt, depth = 0, 2

while q or nq:
    if not q:
        depth -= 1
        if depth:
            q, nq = nq, []
        else:
            break

    c = q.pop()
    for n in graph[c]:
        if not visited[n]:
            cnt += 1
            visited[n] = 1
            nq.append(n)

print(cnt)