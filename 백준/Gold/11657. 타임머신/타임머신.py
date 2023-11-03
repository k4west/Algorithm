import sys
input = sys.stdin.readline
INF = float("inf")

def main():
    N, M = map(int, input().split())
    bus = []
    dist = [INF]*(N+1)
    flag = True

    for i in range(M):
        bus.append(tuple(map(int, input().split())))

    dist[1] = 0
    for i in range(N):
        for a, b, c in bus:
            if dist[a] != INF and dist[b] > dist[a] + c:
                dist[b] = dist[a] + c
                if i == N - 1:
                    flag = False
                    break

    if flag:
        print("\n".join(map(str, (cost if cost != INF else "-1" for cost in dist[2:]))))
    else:
        print('-1')

if __name__ == "__main__":
    main()