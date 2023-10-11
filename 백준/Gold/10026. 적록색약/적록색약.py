import sys

N = int(sys.stdin.readline())
graph = []
for _ in range(N):
    s = sys.stdin.readline().rstrip()
    graph.append(list(s))

c1, c2 = 0, 0
three_dic = {"R": ("G", "B"), "G": ("R", "B"), "B": ("R", "G")}
two_dic = {"R": ("B"), "G": ("B"), "B": ("R", "G")}
d = ((-1, 0), (1, 0), (0, -1), (0, 1)) # 상, 하, 좌, 우

def bfs(dic):
    visited = [[False] * N for _ in range(N)]
    c = 0
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                c += 1
                color = graph[i][j]
                visited[i][j] = True
                q = [(i, j)]
                while q:
                    y, x = q.pop()
                    for dy, dx in d:
                        ny, nx = y + dy, x + dx
                        if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx] and graph[ny][nx] not in dic[color]:
                            q.append((ny, nx))
                            visited[ny][nx] = True
    return c

print(bfs(three_dic), bfs(two_dic))