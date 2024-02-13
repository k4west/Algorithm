def solution(N, number):
    if N == number:
        return 1
    n = str(N)
    q, next_q, i = [n], [], 2
    visit = {n}

    while q:
        for now in q:
            for op in ("", "+", "-"):
                tmp = op.join((now, n))
                if eval(tmp) == number:
                    return i
                elif i < 8 and tmp not in visit:
                    next_q.append(tmp)
                    visit.add(tmp)
            for op in ("*", "//"):
                for t in (now, f"({now})"):
                    tmp = op.join((t, n))
                    if eval(tmp) == number:
                        return i
                    elif i < 8 and tmp not in visit:
                        next_q.append(tmp)
                        visit.add(tmp)
        q, next_q = next_q, []
        i += 1
    return -1