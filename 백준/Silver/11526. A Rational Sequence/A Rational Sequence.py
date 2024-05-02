a = open(0)
def main():
    ans = []
    for _ in range(int(next(a))):
        i, pq = next(a).rstrip().split()
        p, q = map(int, pq.split('/'))
        line = 0
        r = []
        while p != 1 or q != 1:
            if p < q:
                q -= p
                r.append(False)
            else:
                p -= q
                r.append(True)
            line += 1
        j = 1
        if p-1:
            r += [True]*(p-1)
        if q-1:
            r += [False]*(q-1)
        for t in r[::-1]:
            j *= 2
            if not t:
                j -= 1
        n = 2**line - 1 + j
        ans.append(f"{i} {n}")
    print("\n".join(ans))
main()