import sys
input = sys.stdin.readline

def main():
    n = int(input())
    graph = [[] for _ in range(n+1)]
    for _ in range(n-1):
        p, c, w = map(int, input().split())
        graph[p].append((c, w))
        graph[c].append((p, w))

    def dfs(n, e, flag):
        distance = [-1] * (n+1)
        stack = [(e, 0)]
        N, M = 0, 0
        while stack:
            e, d = stack.pop()
            distance[e] = d
            for node, weight in graph[e]:
                if distance[node] == -1:
                    stack.append((node, d + weight))
        if flag:
            x = 0
            for i in range(1, n+1):
                if distance[x] < distance[i]:
                    x = i
            return x
        return max(distance)

    print(dfs(n, dfs(n, 1, True), False))

if __name__ == "__main__":
    main()