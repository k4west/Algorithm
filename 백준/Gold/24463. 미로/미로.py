# 문제 요약
# .: 길
# +: 벽
# 출입구: 가장자리 . : 항상 2개 -> 출입구 찾기
# 최단 경로 외의 .은 @으로 표시 -> 변경하기 : dfs
# 미로 출력

# . -> @으로 변경 후 최단 경로에 .표시하기

def dfs(r, c):
    stack = []
    visited = [[0]*M for _ in range(N)]
    visited[r][c] = 1
    
    while True:
        for dr, dc in d:
            if 0 <= (nr:= r+dr) < N and 0 <= (nc := c+dc) < M and maze[nr][nc] == '@' and not visited[nr][nc]:
                maze[nr][nc] = '.'
                if nr == er and nc == ec:
                    return
                
                visited[nr][nc] = 1
                stack.append((r, c, nr, nc))
                r, c = nr, nc
                break
        else:
            if stack:
                r, c, nr, nc = stack.pop()
                maze[nr][nc] = '@'
            else:
                break

dist = float("inf")
d = ((-1, 0), (1, 0), (0, -1), (0, 1))
N, M = map(int, input().split())
maze = [list(input().replace('.', '@')) for _ in range(N)]

# 출입구 찾기
gate = []

for c in range(M):
    if maze[0][c] == '@':
        gate.append((0, c))
    if maze[N-1][c] == '@':
        gate.append((N-1, c))

for r in range(N):
    if maze[r][0] == '@':
        gate.append((r, 0))
    if maze[r][M-1] == '@':
        gate.append((r, M-1))

# 최단 경로 찾기 & .(@) 표시하기
(sr, sc), (er, ec) = gate
maze[sr][sc] = '.'
dfs(sr, sc)

# 출력
print('\n'.join(''.join(row) for row in maze))