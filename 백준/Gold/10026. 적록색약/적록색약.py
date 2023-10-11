import sys
from collections import deque
sys.setrecursionlimit(10**6)

N = int(sys.stdin.readline())
graph = []
for _ in range(N):
    s = sys.stdin.readline().rstrip()
    graph.append(list(s))

c1, c2 = 0, 0
visited1 = [[False] * N for _ in range(N)]
visited2 = [[False] * N for _ in range(N)]
d = ((-1, 0), (1, 0), (0, -1), (0, 1)) # 상, 하, 좌, 우

def three(y0, x0):
    color = graph[y0][x0]
    visited1[y0][x0] = True
    q = deque([(y0, x0)])
    while q:
        y, x = q.popleft()
        for dy, dx in d:
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < N and not visited1[ny][nx]:
                if graph[ny][nx] == color:
                    q.append((ny, nx))
                    visited1[ny][nx] = True

def two(y0, x0):
    color = graph[y0][x0]
    visited2[y0][x0] = True
    q = deque([(y0, x0)])
    while q:
        y, x = q.popleft()
        for dy, dx in d:
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < N and not visited2[ny][nx]:
                if graph[ny][nx] == 'B' == color or graph[ny][nx] != 'B' and color != 'B':
                    q.append((ny, nx))
                    visited2[ny][nx] = True

for i in range(N):
    for j in range(N):
        if not visited1[i][j]:
            c1 += 1
            three(i, j)

for i in range(N):
    for j in range(N):
        if not visited2[i][j]:
            c2 += 1
            two(i, j)

print(c1, c2)