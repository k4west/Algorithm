import sys
input = sys.stdin.readline

R, C = map(int, input().split())
L = R*C
graph = []
for _ in range(R):
    graph.extend(list(map(lambda x:1 << ord(x)-65, input().rstrip())))

ans = 1

def dfs(d, p, v):
    global ans
    i, j = p//C, p%C
          
    if ans < d: 
        ans = d
        if ans == 26:
            print(26)
            exit()
    d += 1
    if (i+1) < R and not (w:=graph[k:=p+C])&v:
        dfs(d, k, v|w)
    if 0 <= (i-1) and not (w:=graph[k:=p-C])&v:
        dfs(d, k, v|w)
    if (j+1) < C and not (w:=graph[k:=p+1])&v:
        dfs(d, k, v|w)
    if 0 <= (j-1) and not (w:=graph[k:=p-1])&v:
        dfs(d, k, v|w)

dfs(1, 0, graph[0])
print(ans)