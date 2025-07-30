import sys
sys.setrecursionlimit(10**5)

def dfs(r, c, o, v):
    t = graph[r][c]
    if t == 'o':
        o += 1
    elif t == 'v':
        v += 1
    graph[r][c] = '#'

    for dr, dc in d:
        nr, nc = r+dr, c+dc
        if 0 <= nr < R and 0 <= nc < C and graph[nr][nc] != '#':
            o, v = dfs(nr, nc, o, v)
    return o, v


ans = [0, 0]    # [sheep, wolves]
d = ((-1, 0), (1, 0), (0, -1), (0, 1))
R, C = map(int, input().split())
graph = [[*input()] for _ in range(R)]

for r in range(R):
    for c in range(C):
        # 울타리(=#)가 아니면 모두 탐색
        if graph[r][c] != '#':
            o, v = dfs(r, c, 0, 0)
            if o > v:
                v = 0
            else:
                o = 0
            ans[0] += o
            ans[1] += v
print(*ans)