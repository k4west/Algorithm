import sys
input = sys.stdin.readline
INF = float("inf")

def main():
    N, M = map(int, input().split())
    bus = [dict() for _ in range(N+1)]
    dist = [INF]*(N+1)
    flag = True

    for i in range(M):
        a, b, c = map(int, input().split())
        if c < bus[a].get(b, INF):
            bus[a][b] = c

    dist[1] = 0
    for i in range(N):
        for a in range(1, N+1):
            if dist[a] == INF:
                continue
            for b, c in bus[a].items():
                if dist[b] <= dist[a] + c:
                    continue
                dist[b] = dist[a] + c
                if i == N - 1:
                    flag = False
                    break

    if flag:
        for cost in dist[2:]:
            if cost == INF:
                print("-1")
            else: print(cost)
    else:
        print(-1)

if __name__ == "__main__":
    main()