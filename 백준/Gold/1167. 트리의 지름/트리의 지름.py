import sys
input = sys.stdin.readline

def main():
    V = int(input())
    graph = [[] for _ in range(V+1)]
    for _ in range(V):
        a, *li = map(int, input().split())
        for b, c in zip(li[::2], li[1::2]):
            graph[a].append((b, c))

    def dfs(s, V):
        dist = 0
        v = [False]*(V+1)
        stack = [(s, 0)]
        while stack:
            n0, d0 = stack.pop()
            if dist < d0:
                s, dist = n0, d0
            v[n0] = True
            for n1, d1 in graph[n0]:
                if not v[n1]:
                    stack.append((n1, d0 + d1))
        return s, dist

    print(dfs(dfs(1, V)[0], V)[1])

if __name__ == "__main__":
    main()