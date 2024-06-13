def solution(k, n, reqs):
    d = {}
    for a, b, c in reqs:
        if c not in d:
            d[c] = []
        d[c].append([a, b])
    n -= k
    types = {c:1 for c in d.keys()}
    t = [0]*k
    for c in d.keys():
        tt = 0
        mentor = [0]
        for a, b in d[c]:
            if a >= (i:=min(mentor)):
                mentor[mentor.index(i)] = a+b
            else:
                mentor[mentor.index(i)] += b
                tt += i-a
        t[c-1] = tt
    while n and sum(t):
        tt = [0]*k
        for c, m in types.items():
            mentor = [0]*(m+1)
            for a, b in d[c]:
                if a >= (i:=min(mentor)):
                    mentor[mentor.index(i)] = a+b
                else:
                    mentor[mentor.index(i)] += b
                    tt[c-1] += i-a
        n -= 1
        diff = 0
        for i, (j, jj) in enumerate(zip(t, tt)):
            if j-jj >= diff:
                diff = j-jj
                x = i
        types[x+1] += 1
        t[x] = tt[x]
    return sum(t)