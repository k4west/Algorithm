import sys

def main():
    INF = float('inf')
    input = sys.stdin.readline
    N = int(input())
    M = int(input())
    graph = [[INF]*(N+1) for _ in range(N+1)]

    for _ in range(M):
        i, j, k = map(int, input().split())
        if k < graph[i][j]:
            graph[i][j] = k

    for i in range(1, N+1):
        graph[i][i] = 0

    for node in range(1, N+1):
        for i in range(1, N+1):
            for j in range(1, N+1):
                if graph[i][node] + graph[node][j] < graph[i][j]:
                    graph[i][j] = graph[i][node] + graph[node][j]

    print("\n".join([" ".join(map(str, row[1:])) for row in graph[1:]]).replace('inf', '0'))

if __name__ == '__main__':
    main()