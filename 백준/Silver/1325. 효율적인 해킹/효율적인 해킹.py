a = open(0)
N, M = map(int, next(a).split())
graph = [[] for _ in range(N+1)]
li = [0]*(N+1)
for _ in range(M):
    A, B = map(int, next(a).split())
    graph[B].append(A)
for i in range(1, N+1):
    q = [i]
    c = 0
    v = [0]*(N+1)
    v[i] = 1
    while q:
        j = q.pop()
        for k in graph[j]:
            if not v[k]:
                q.append(k)
                v[k] = 1
                c += 1
    li[i] = c
m = max(li)
print(*[i for i in range(1, N+1) if li[i]==m])