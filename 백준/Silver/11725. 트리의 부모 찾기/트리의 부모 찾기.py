import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N+1)]
ans = [[] for _ in range(N+1)]
for _ in range(N-1):
    i, j = map(int, input().split())
    graph[i].append(j)
    graph[j].append(i)

def dfs(i):
    for n in graph[i]:
        if not ans[n]: 
            ans[n] = i
            dfs(n)

dfs(1)
print("\n".join(map(str, ans[2:])))