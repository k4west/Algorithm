import sys
input = sys.stdin.readline

def main():
    V = int(input())
    graph = [[] for _ in range(V+1)]
    for _ in range(V):
        a, *li = map(int, input().split())
        for b, c in zip(li[::2], li[1::2]):
            graph[a].append((b, c))

    dist = [-1]*(V+1)
    def dfs(s):
        stack = [(s, 0)]
        while stack:
            n0, d0 = stack.pop()
            dist[n0] = d0
            for n1, d1 in graph[n0]:
                if dist[n1] == -1:
                    stack.append((n1, d0 + d1))
        x = 0
        for i in range(1, V+1):
            if dist[x] < dist[i]:
                x = i
        return x

    e = dfs(1)
    dist = [-1]*(V+1)
    print(dist[dfs(e)])

if __name__ == "__main__":
    main()