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
            for next, d in graph[node]:
                n_dist = dist + d
                if n_dist < distance[next]:
                    distance[next] = n_dist
                    heappush(q, (n_dist, next))
    
    f(s)
    for d in distance[1:]:
        if d != INF: print(f'{d}\n')
        else: print('INF\n')

if __name__ == "__main__":
    main()