def solution(n, m, section):
    c, t = 0, 0
    li = [0] * (n+1)
    if m == 1:
        return len(section)
    else:
        for i in section:
            li[i] = 1
        for i in range(1,n+1):
            if t:
                t -= 1
            elif li[i]:
                c += 1
                t = m-1
    return c