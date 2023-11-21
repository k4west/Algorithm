import sys
input = sys.stdin.readline

R, C = map(int, input().split())
graph = []
for _ in range(R):
    graph.append(list(input().rstrip()))

v, ans = {graph[0][0]}, 1
def dfs(d, i, j):
    global ans

    def f(a, c, x, y):
        v.add(a)
        dfs(c, x, y)
        v.remove(a)
        
    if ans < d: ans = d
    if (ni:=i+1) < R and not (k:=graph[ni][j]) in v:
        f(k, d+1, ni, j)
    if 0 <= (ni:=i-1) and not (k:=graph[ni][j]) in v:
        f(k, d+1, ni, j)
    if (nj:=j+1) < C and not (k:=graph[i][nj]) in v:
        f(k, d+1, i, nj)
    if 0 <= (nj:=j-1) and not (k:=graph[i][nj]) in v:
        f(k, d+1, i, nj)

dfs(1, 0, 0)
print(ans)