import sys
input = sys.stdin.readline

R, C = map(int, input().split())
graph = []
for _ in range(R):
    graph.append(list(input().rstrip()))

v, ans = [False]*26, 1
v[ord(graph[0][0])-65] = True

def dfs(d, i, j):
    global ans

    def f(n, c, x, y):
        v[n] = True
        dfs(c, x, y)
        v[n] = False
        
    if ans < d: ans = d
    if (ni:=i+1) < R and not v[k:=ord(graph[ni][j])-65]:
        f(k, d+1, ni, j)
    if 0 <= (ni:=i-1) and not v[k:=ord(graph[ni][j])-65]:
        f(k, d+1, ni, j)
    if (nj:=j+1) < C and not v[k:=ord(graph[i][nj])-65]:
        f(k, d+1, i, nj)
    if 0 <= (nj:=j-1) and not v[k:=ord(graph[i][nj])-65]:
        f(k, d+1, i, nj)

dfs(1, 0, 0)
print(ans)