from heapq import heappop, heappush
def solution(alp, cop, problems):
    ma, mc = 0, 0
    for aq, cq, _, _, _ in problems:
        if ma < aq:
            ma = aq
        if mc < cq:
            mc = cq
    problems += [[0, 0, 1, 0, 1], [0, 0, 0, 1, 1]]
    
    dp = {(alp, cop): 0}
    q = [(0, alp, cop)]
    while q:
        t, a, c = heappop(q)
        if a >= ma and c >= mc:
            return t
        for aq, cq, ad, cd, ct in problems:
            if a >= aq and c >= cq:
                nt, na, nc = t+ct, min(a+ad, 150), min(c+cd, 150)
                if nt < dp.get((na, nc), 30000000):
                    dp[(na, nc)] = nt
                    heappush(q, (nt, na, nc))
    return answer