def solution(s):
    a, b, c, i = 0, 0, 0, 0
    n, t = len(s), s[i]
    s += ' '
    while i < n:
        if s[i] == t:
            a += 1
        else: b += 1
        i += 1
        if a == b and a != 0:
            a, b = 0, 0
            c += 1
            t = s[i]
    return c+1 if a else c