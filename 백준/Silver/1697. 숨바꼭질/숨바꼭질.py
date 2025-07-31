def bfs():
    q, nq = [K], []
    t = 0
    v = set()
    while q or nq:
        if not q:
            q, nq = nq, []
            t += 1
        k = q.pop()
        if k == N:
            return t

        if not k % 2 and k//2 not in v:
            n = k//2
            v.add(n)
            nq.append(n)

        for n in (k-1, k+1):
            if n not in v:
                v.add(n)
                nq.append(n)        

N, K = map(int, input().split())
print(bfs())