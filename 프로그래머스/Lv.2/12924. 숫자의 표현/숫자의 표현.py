def solution(n):
    c = 1
    arr = list(range(n))
    t = s = 1
    for e in range(2, n):
        t += e
        while t > n:
            t -= s
            s += 1
        if t == n:
            c += 1
    return c