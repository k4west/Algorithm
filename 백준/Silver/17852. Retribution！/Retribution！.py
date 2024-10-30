def dist(i, loc):
    x0, y0 = loc
    return [(((x1-x0)**2+(y1-y0)**2)**.5, j, i) for j, (x1, y1) in enumerate(judges)]

def sum_d(n):
    s = 0
    locs = sum([dist(i, [*map(int, next(a).split())]) for i in range(n)], [])
    locs.sort()
    jud_visit = set()
    loc_visit = set()
    for d, i, j in locs:
        if i in jud_visit or j in loc_visit:
            continue
        jud_visit.add(i)
        loc_visit.add(j)
        s += d
    return s

if __name__ == '__main__':
    a=open(0)
    n, m, p = map(int, next(a).split())
    judges = [[*map(int, next(a).split())] for _ in range(n)]
    print(sum_d(m)+sum_d(p))