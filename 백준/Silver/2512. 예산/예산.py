def bi_search(s, e, li):
    if sum(li) <= M:
        return max(li)
    
    while s <= e:
        m = (s + e) // 2
        
        sm = 0
        for r in li:
            if r < m:
                sm += r
            else:
                sm += m

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
print(bi_search(0, 100000, req))