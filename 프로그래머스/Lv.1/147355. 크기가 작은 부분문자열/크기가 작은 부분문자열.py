def solution(t, p):
    n, p, c = len(p), int(p), 0
    for i in range(len(t)-n+1):
        if int("".join(t[i:i+n])) <= p:
            c +=1
    
    # s = e = 0
    # for i in t:
    #     e += 1
    #     if e-s == n:
    #         if int("".join(t[s:e])) <= p:
    #             c += 1
    #         s += 1
    return c