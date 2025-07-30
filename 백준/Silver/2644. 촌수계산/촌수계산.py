def bfs(n):
    # 초기화
    dist = 0
    visited[n] = 1
    q, nq = [n], []

    while q:
        for n in q:
            for nn in graph[n]:
                if nn == G:
                    return dist + 1
                
                if not visited[nn]:
                    nq.append(nn)
                    visited[nn] = 1
        
        q, nq = nq, []
        dist += 1
    
    return -1


n = int(input())
graph = [[] for _ in range(n+1)]
visited = [0]*(n+1)

S, G = map(int, input().split())
m = int(input())
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

print(bfs(S))
