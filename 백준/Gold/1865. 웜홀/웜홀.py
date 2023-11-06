import sys
input = sys.stdin.readline

TC = int(input())
ans = ["NO"]*(TC)
for i in range(TC):
    N, M, W = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    dist0 = [0]*(N+1)
    dist1 = [0]*(N+1)

    # 도로(방향x)
    for _ in range(M):
        S, E, T = map(int, input().split())
        graph[S].append((E, T))
        graph[E].append((S, T))
    
    # 웜홀(방향o)
    for _ in range(W):
        S, E, T = map(int, input().split())
        graph[S].append((E, -T))
    
    li = list(range(1, N+1))
    v = set()
    while li:
        tmp = []
        if (tu:= tuple(li)) in v:
            ans[i] = "YES"
            break
        v.add(tu)
        for s in li:
            for e, t in graph[s]:
                if (nt:= dist0[s] + t) < dist1[e]:
                    dist1[e] = nt
                    tmp.append(e)
        for s in tmp:
            dist0[s] = dist1[s]
        li = tmp

print("\n".join(ans))