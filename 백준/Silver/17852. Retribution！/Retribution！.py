def dist(i, loc):
    x0, y0 = loc
    return [(((x1-x0)**2+(y1-y0)**2)**.5, j, i) for j, (x1, y1) in enumerate(judges)]

def sum_d(t):
    s = 0
    locs = sum([dist(i, [*map(int, next(a).split())]) for i in range(t)], [])
    locs.sort()
    jud_visit = [0]*n
    loc_visit = [0]*t
    for d, i, j in locs:
        if jud_visit[i] or loc_visit[j]:
            continue
        jud_visit[i] = 1
        loc_visit[j] = 1
        s += d
    return s

if __name__ == '__main__':
    a=open(0)
    n, m, p = map(int, next(a).split())
    judges = [[*map(int, next(a).split())] for _ in range(n)]
    print(sum_d(m)+sum_d(p))