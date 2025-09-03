def roll(d, ori):
    t, b, n, s, w, e = ori

    if d == 0:
        return s, n, t, b, w, e
    if d == 1:
        return n, s, b, t, w, e
    if d == 2:
        return e, w, n, s, t, b
    if d == 3:
        return w, e, n, s, b, t


def check(st):
    v = {}
    r0, c0 = min(st)
    
    v[(r0, c0)] = INDEXES[0]
    q = [(r0, c0, INDEXES)]
    
    while q:
        r, c, ori = q.pop()
        for d in range(4):
            nr, nc = r+D[d][0], c+D[d][1]
            
            if (nr, nc) in st:
                nori = roll(d, ori)
                top = nori[0]

                if (nr, nc) in v:
                    if v[(nr, nc)] != top:
                        return False
                    continue
                
                v[(nr, nc)] = top
                q.append((nr, nc, nori))
    
    return len(set(v.values())) == 6

ans = []
result = ["no", "yes"]
INDEXES = (1, 6, 2, 5, 3, 4)  # t, b, n, s, w, e
D = ((-1, 0), (1, 0), (0, -1), (0, 1))

for _ in range(3):
    pos = set()
    for i in range(6):
        for j, k in enumerate(input().split()):
            if k == '1':
                pos.add((i, j))
    ans.append(result[check(pos)])

print("\n".join(ans))