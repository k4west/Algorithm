def bfs(a):
    q = [(a, 1)]
    v = set()

    while q:
        a, cnt = q.pop(0)
        for op in ops:
            b = op(a)
            if b == B:
                return cnt + 1
            if b not in v and b < B:
                v.add(b)
                q.append((b, cnt+1))
    return -1


A, B = map(int, input().split())
ops = [lambda x: 2*x, lambda x: x*10 + 1]
print(bfs(A))