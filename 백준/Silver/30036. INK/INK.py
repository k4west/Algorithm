def check(i, j):
    return 0 <= i < N and 0 <= j < N


def move(dr, dc):
    global box
    
    r, c = box
    nr = r + dr
    nc = c + dc
    if check(nr, nc) and stage[nr][nc] == ".":
        stage[r][c] = '.'
        stage[nr][nc] = '@'
        box = (nr, nc)


def jump(): # bfs
    r, c = box
    m = ink_amount[ink]
    if m == 0:
        return
    
    v = {(r, c)}
    q, nq = [(r, c)], []
    
    while q or nq:
        if not q:
            m -= 1
            if not m:
                break
            q, nq = nq, []
            
        r, c = q.pop()
        for dr, dc in d:
            nr, nc = r+dr, c+dc
            if check(nr, nc) and (nr, nc) not in v:
                v.add((nr, nc))
                if stage[nr][nc] != ".":
                    stage[nr][nc] = ink
                nq.append((nr, nc))

    ink_amount[ink] = 0


move_dict = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}
*d, = move_dict.values()

I, N, K = map(int, input().split())
inks = list(input())  # 점프(J) 할 때마다 색상이 바뀜 -> idx로 관리하자
ink_amount = {ink: 0 for ink in inks}

stage = []
box = (0, 0)
for r in range(N):
    row = list(input())
    stage.append(row)
    
    for c in range(N):
        if row[c] == '@':
            box = (r, c)

idx = 0
ink = inks[0]

for cmd in input():
    if cmd in move_dict:
        move(*move_dict[cmd])
    elif cmd == 'j':
        ink_amount[ink] += 1
    else:
        jump()
        idx = (idx+1)%I
        ink = inks[idx]

print('\n'.join(''.join(row) for row in stage))