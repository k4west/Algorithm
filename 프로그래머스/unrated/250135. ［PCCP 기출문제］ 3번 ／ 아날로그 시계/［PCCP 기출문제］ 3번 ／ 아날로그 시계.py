def solution(h1, m1, s1, h2, m2, s2):
    c = 0
    ss, ms, hs = 6*s1, 6*m1 + 0.1*s1, 30*(h1%12) + 0.5*m1 + (1/120)*s1
    if ss == ms or ss == hs:
        c += 1
    while h1 < h2 or m1 < m2 or s1 < s2:
        s1 += 1
        if s1 == 60:
            m1 += 1
            s1 = 0
        if m1 == 60:
            h1 += 1
            m1 = 0
            
        se, me, he = 6*s1, 6*m1 + 0.1*s1, 30*(h1%12) + 0.5*m1 + (1/120)*s1
        st, mt, ht = se, me, he
        if not st:
            st = 360
        if not mt:
            mt = 360
        if not ht:
            ht = 360
        
        if ss < ms < mt <= st:
            c += 1
        if ss < hs < ht <= st:
            c += 1
        if s1 == m1 == 0 and not h1%12:
            c -= 1

        ss, ms, hs = se, me, he
    
    return c