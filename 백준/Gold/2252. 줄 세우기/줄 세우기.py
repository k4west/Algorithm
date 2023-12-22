import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
    
def main():
    N, M = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    v, line = [False]*(N+1), []

    for _ in range(M):
        a, b = map(int, input().split())
        graph[b].append(a)

    def dfs(n):
        if v[n]: return
        v[n] = True
        for s in graph[n]: dfs(s)
        line.append(str(n))

    for i in range(1, N+1): dfs(i)
    print(" ".join(line))

if __name__ == "__main__":
    main()