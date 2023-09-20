def solution(n, m, section):
    c, pre = 1, section[0]
    for now in section[1:]:
        if now - pre >= m:
            c +=1
            pre = now
    return c