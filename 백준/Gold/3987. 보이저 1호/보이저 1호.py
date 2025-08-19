# \: 위 <-> 왼; 아래 <-> 오른
# /: 위 <-> 오른; 아래 <-> 왼

d = {"U": (-1, 0), "R": (0, 1), "D": (1, 0), "L": (0, -1)}
N, M = map(int, input().split())
graph = [list(input()) for _ in range(N)]
r0, c0 = map(int, input().split())

time = {}
flag = False

for k, (dr, dc) in d.items():
    r, c = r0-1, c0-1
    v = [[0]*M for _ in range(N)]
    v[r][c] = 1 << (2*dr+dc + 2 + (2*dr+dc < 0))

    t = 0
    while True:
        nr, nc = r+dr, c+dc
        t += 1
        if 0 <= nr < N and 0 <= nc < M:
            dd = 2*dr+dc + 2 + (2*dr+dc < 0)
            if (v[nr][nc] >> dd) & 1:
                flag = True
                break

            if graph[nr][nc] == 'C':
                break

            if graph[nr][nc] == '\\':
                v[nr][nc] |= 1 << dd
                dr, dc = dc, dr
            elif graph[nr][nc] == '/':
                v[nr][nc] |= 1 << dd
                dr, dc = -dc, -dr

            r, c = nr, nc
        else:
            break

    if flag:
        break
    else:
        time[k] = t

if flag:
    print(k)
    print("Voyager")
else:
    ans = ''
    m = 0
    for k, v in time.items():
        if m < v:
            m = v
            ans = k
    print(ans)
    print(m)
