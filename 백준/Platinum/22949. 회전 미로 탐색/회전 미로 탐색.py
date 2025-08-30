def rotate(r, c, div):
    diff_r, diff_c = 4*((div-1)//k), 4*((div-1)%k)
    return c - diff_c + diff_r, 3 - r + diff_r + diff_c


def bfs(r, c, div):
    t = 1
    v = [[[0]*K for _ in range(K)] for _ in range(4)]
    v[0][r][c] = 1
    q, nq = [(r, c, r, c, div, 0)], []
    
    while q:
        for r, c, y, x, div, offset in q:
            for i in range(5):
                if i:
                    dr, dc = D[i-1]
                    dy, dx = D[(i+offset-1)&3]
                else:
                    dr = dc = dy = dx = 0
                nr, nc = r + dr,  c + dc
                ny, nx = y + dy, x + dx

                if 0 <= nr < K and 0 <= nc < K:
                    nxt_div = k * (nr >> 2) + (nc >> 2) + 1
                    if div == nxt_div:
                        nxt_offset = (offset + 1) & 3
                    else:
                        nxt_offset = 1
                        ny, nx = nr, nc

                    if MAZE[ny][nx] == '#':
                        continue
                    if MAZE[ny][nx] == 'E':
                        return t

                    nr, nc = rotate(nr, nc, nxt_div)
                    idx = nr*K + nc
                    
                    if v[nxt_offset][nr][nc]:
                        continue
                    
                    v[nxt_offset][nr][nc] = 1
                    nq.append((nr, nc, ny, nx, nxt_div, nxt_offset))

        q, nq = nq, []
        t += 1
    return -1


D = ((-1, 0), (0, -1), (1, 0), (0, 1))  # ↑ ← ↓ →
k = int(input())
K = 4*k
MAZE = [list(input()) for _ in range(K)]

si = sj = sdiv = 0
for i in range(K):
    for j in range(K):
        if MAZE[i][j] == 'S':
            si, sj = i, j
            sdiv = k*(i >> 2)+(j >> 2)+1
            break
    if sdiv:
        break

print(bfs(si, sj, sdiv))
