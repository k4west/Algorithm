import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
graph, virus = [], []
a = -3
ans = 0

for i in range(N):
    graph.append(list(map(int, input().split())))
    for j, k in enumerate(graph[i]):
        if not k:
            a += 1
        elif k == 2:
            virus.append((i, j))
        
def bfs():
    global a
    lab = [[e for e in row] for row in graph]
    # q = deque([row for row in virus])
    q = deque(virus.copy())
    m = 0
    while q:
        r, c = q.popleft()
        if (nr:=r+1) < N and not lab[nr][c]:
            lab[nr][c] = 2
            q.append((nr, c))
            m += 1

        if 0 <= (nr:=r-1) and not lab[nr][c]:
            lab[nr][c] = 2
            q.append((nr, c))
            m += 1

        if (nc:=c+1) < M and not lab[r][nc]:
            lab[r][nc] = 2
            q.append((r, nc))
            m += 1

        if 0 <= (nc:=c-1) and not lab[r][nc]:
            lab[r][nc] = 2
            q.append((r, nc))
            m += 1
    return a-m

def wall(w):
    global ans
    if not w:
        ans = max(ans, bfs())
        return

    for i in range(N):
        for j in range(M):
            if not graph[i][j]:
                graph[i][j] = 1
                wall(w-1)
                graph[i][j] = 0

wall(3)
print(ans)