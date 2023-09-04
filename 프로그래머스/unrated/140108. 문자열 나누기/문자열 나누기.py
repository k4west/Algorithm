def solution(s):
    a, b, c = 0, 0, 0
    for i in s:
        if a == b:
            c += 1
            t = i
        if i == t:
            a += 1
        else: b += 1
    return c