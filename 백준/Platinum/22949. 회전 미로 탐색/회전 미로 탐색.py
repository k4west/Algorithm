from collections import deque


def seen(arr, idx):
    return (arr[idx >> 3] >> (idx & 7)) & 1


def mark(arr, idx):
    arr[idx >> 3] |= (1 << (idx & 7))


def get_div(r, c):
    return k*(r >> 2)+(c >> 2)+1


def rotate_pos(r, c):
    diff_r, diff_c = (r >> 2) << 2, (c >> 2) << 2
    return (c & 3) + diff_r, 3 - (r & 3) + diff_c


def rotate_maze(maze):
    rotated = [row[:] for row in maze]
    for r in range(K):
        for c in range(K):
            nr, nc = rotate_pos(r, c)
            rotated[nr][nc] = maze[r][c]
    return rotated


def bfs(r, c, arr):
    v = [bytearray(BYTES) for _ in range(4)]
    mark(v[0], r*K+c)
    q = deque([(r, c, 0, 0)])
    
    while q:
        r, c, offset, t = q.popleft()
        if arr[offset][r][c] == 'E':
            return t
        
        div = get_div(r, c)
        for dr, dc in D:
            nr, nc = r+dr, c+dc

            if 0 <= nr < K and 0 <= nc < K:
                nxt_div = get_div(nr, nc)
                if div == nxt_div:
                    nxt_offset = (offset + 1) & 3
                else:
                    nxt_offset = 1
                
                nr, nc = rotate_pos(nr, nc)
                idx = nr*K + nc
                
                if seen(v[nxt_offset], idx) or arr[nxt_offset][nr][nc] == '#':
                    continue
                
                mark(v[nxt_offset], idx)
                q.append((nr, nc, nxt_offset, t+1))
    return -1


D = ((0, 0), (-1, 0), (0, -1), (1, 0), (0, 1))  # ↑ ← ↓ →
k = int(input())
K = 4*k
BYTES = (K*K+7) >> 3
MAZE = [list(input()) for _ in range(K)]

si = sj = sdiv = 0
for i in range(K):
    for j in range(K):
        if MAZE[i][j] == 'S':
            si, sj = i, j
            break
    if sdiv:
        break

ROT_MAZE = [[row[:] for row in MAZE]]
for _ in range(3):
    MAZE = rotate_maze(MAZE)
    ROT_MAZE.append(MAZE)

print(bfs(si, sj, ROT_MAZE))
