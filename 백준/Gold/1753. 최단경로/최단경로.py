from sys import stdin, stdout
from heapq import heappop, heappush

def main():
    input = stdin.readline
    print = stdout.write

    INF = float('inf')
    V, E = map(int, input().split())
    s = int(input())
    graph = [[] for _ in range(V+1)]
    distance = [INF] * (V+1)
    distance[s] = 0

    for _ in range(E):
        i, j, k = map(int, input().split())
        graph[i].append((j, k))

    def f(s):
        q = [(0, s)]
        while q:
            dist, node = heappop(q)
            if dist > distance[node]:
                continue
            for n, d in graph[node]:
                n_dist = dist + d
                if n_dist < distance[n]:
                    distance[n] = n_dist
                    heappush(q, (n_dist, n))
    
    f(s)
    print("\n".join(map(str, [d if d != INF else 'INF' for d in distance[1:]])))

if __name__ == "__main__":
    main()