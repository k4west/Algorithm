import sys
input = sys.stdin.readline
INF = 25000000

TC = int(input())
ans = [""]*(TC)
for i in range(TC):
    N, M, W = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    dist = [INF]*(N+1)

    # 도로(방향x)
    for _ in range(M):
        S, E, T = map(int, input().split())
        graph[S].append((E, T))
        graph[E].append((S, T))
    
    # 웜홀(방향o)
    for _ in range(W):
        S, E, T = map(int, input().split())
        graph[S].append((E, -T))
    
    dist[1] = 0
    for _ in range(N-1):
        for s in range(1, N+1):
            for e, t in graph[s]:
                if dist[s] + t < dist[e]:
                    dist[e] = dist[s] + t
    
    for s in range(1, N+1):
        for e, t in graph[s]:
            if dist[s] + t < dist[e]:
                ans[i] += "YES"
                break
        if ans[i]:
            break
    else:
        ans[i] += "NO"

print("\n".join(ans))
