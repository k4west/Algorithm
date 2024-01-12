def solution(t, p):
    n = len(p)
    p = int(p)
    s = e = c = 0
    for i in t:
        e += 1
        if e-s == n:
            if int("".join(t[s:e])) <= p:
                c += 1
            s += 1
    return c