ans = 0
N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [0]*(N+1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


for cur in range(1, N+1):
    stack = [(cur, 0)]
    visited[cur] = 1
    cnt = 0

    while stack:
        if cnt == 4:
            ans = 1
            break
        
        cur, idx = stack.pop()
        if idx == len(graph[cur]):
            visited[cur] = 0
            cnt -= 1
            continue
        
        nxt = graph[cur][idx]
        stack.append((cur, idx+1))
        
        if not visited[nxt]:
            visited[nxt] = 1
            cnt += 1
            stack.append((nxt, 0))
    
    if ans:
        break
    visited[cur] = 0

print(ans)