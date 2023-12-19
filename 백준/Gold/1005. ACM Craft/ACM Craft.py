import sys
from heapq import heappop, heappush
input = sys.stdin.readline

def main():
    for _ in range(int(input())):
        N, K = map(int, input().split())
        graph = [[0, [], 0] for _ in range(N)]
        dist = list(map(int, input().split()))
        for _ in range(K):
            a, b = map(int, input().split())
            graph[a-1][1].append(b-1)
            graph[b-1][0] += 1
        W = int(input()) - 1
            
        q = []
        for i in range(N):
            if not graph[i][0]:
                heappush(q, (0, i))
                graph[i][2] = dist[i]

        while q:
            _, n0 = heappop(q)
            for n1 in graph[n0][1]:
                graph[n1][0] -= 1
                if graph[n1][2] < (d:= dist[n1] + graph[n0][2]):
                    graph[n1][2] = d
                if not graph[n1][0]:
                    heappush(q, (graph[n1][2], n1))

        print(graph[W][2])
            
if __name__ == "__main__":
    main()