def bfs():
    jump = 0

    v = [[0]*M for _ in range(N)]
    q, nq = [(x1, y1)], []
    v[x1][y1] = 1

    while q or nq:
        if not q:
            jump += 1
            q, nq = nq, []

        r, c = q.pop()
        for dr, dc in d:
            nr, nc = r + dr, c + dc

            while 0 <= nr < N and 0 <= nc < M and not v[nr][nc]:
                v[nr][nc] = 1

                if room[nr][nc] == '#':
                    return jump+1
                elif room[nr][nc] == '1':
                    nq.append((nr, nc))
                    room[nr][nc] = '0'
                    break
                else:
                    q.append((nr, nc))

                nr, nc = r + dr, c + dc


d = ((-1, 0), (1, 0), (0, -1), (0, 1))
N, M = map(int, input().split())
x1, y1, x2, y2 = map(lambda x: int(x)-1, input().split())
room = [list(input()) for _ in range(N)]

print(bfs())