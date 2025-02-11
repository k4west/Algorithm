def solution(mats, park):
    rows = len(park)
    columns = len(park[0])
    for n in sorted(mats, reverse=True):
        for r in range(rows-n+1):
            for c in range(columns-n+1):
                if set(sum([i[c:c+n] for i in park[r:r+n]], [])) == {"-1"}:
                    return n
    return -1