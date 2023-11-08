import sys
input = sys.stdin.readline

def main():
    V = int(input())
    graph = [[] for _ in range(V+1)]
    for _ in range(V):
        a, *li = map(int, input().split())
        for b, c in zip(li[::2], li[1::2]):
            graph[a].append((b, c))

    def dfs(s):
        dist = 0
        v = set()
        stack = [(s, 0)]
        while stack:
            n0, d0 = stack.pop()
            if dist < d0:
                dist = d0
                s = n0
            v.add(n0)
            for n1, d1 in graph[n0]:
                if n1 not in v:
                    stack.append((n1, d0 + d1))
        return s, dist

    print(dfs(dfs(1)[0])[1])

if __name__ == "__main__":
    main()