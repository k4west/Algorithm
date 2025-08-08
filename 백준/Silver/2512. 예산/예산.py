def bi_search(s, e, li):
    while s <= e:
        m = (s + e) // 2
        sm = sum(min(r, m) for r in li)

        if sm == M:
            return m
        elif sm < M:
            s = m + 1
        else:
            e = m - 1
    return s-1


N = int(input())
*req, = map(int, input().split())
M = int(input())
print(bi_search(0, max(req), req))