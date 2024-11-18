def candi(a, b, c):
    A, B, C = buckets
    for i, j, k in [(max(a - (B - b), 0), min(B, a + b), c), (max(a - (C - c), 0), b, min(C, a + c)), (min(A, a + b), max(b - (A - a), 0), c), (a, max(b - (C - c), 0), min(C, b + c)), (min(A, a + c), b, max(c - (A - a), 0)), (a, min(B, b + c), max(c - (B - b), 0))]:
        if not (i, j, k) in v:
            v.add((i, j, k))
            yield (i, j, k)
    
def bfs(a, b, c):
    q = [[a, b, c]]
    while q:
        a, b, c = q.pop()
        if not a:
            r[c] = 1
        for na, nb, nc in candi(a, b, c):
            q.append((na, nb, nc))

if __name__=="__main__":
    buckets = [*map(int, input().split())]
    C = buckets[2]
    r = [0 for _ in range(C+1)]
    v = set()
    v.add((0, 0, C))
    bfs(0, 0, C)
    print(*[i for i in range(C+1) if r[i]])