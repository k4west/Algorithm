moveD = ((0, 1), (-1, 1), (-1, 0), (0, -1), (1, -1), (1, 0))
nearD = ((-1, 0), (1, 0), (0, -1), (0, 1), (-1, 1), (1, -1))
steps = [1, 0, 1, 1, 1, 1]
r = c = 59
TILE = [[0]*119 for _ in range(119)]
li = [0]*10001
MATRIALS = set(range(1, 6))
matrials = {m: 0 for m in range(1, 6)}

move_idx = 0
step = 0
for idx in range(1, 10001):
    near = {TILE[r+dr][c+dc] for dr, dc in nearD}
    candi = MATRIALS - near
    n, cnt = 0, 10000
    for m in candi:
        t = matrials[m]
        if cnt > t:
            cnt = t
            n = m
    li[idx] = TILE[r][c] = n
    matrials[n] += 1
    dr, dc = moveD[move_idx]
    r, c = r+dr, c+dc
    step += 1
    while steps[move_idx] <= step:
        steps[move_idx] += 1
        move_idx = (move_idx+1) % 6
        step = 0

print("\n".join(map(str, (li[int(input())] for _ in range(int(input()))))))
