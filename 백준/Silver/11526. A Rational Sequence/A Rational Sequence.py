a = open(0)
def main():
    ans = []
    for _ in range(int(next(a))):
        i, pq = next(a).rstrip().split()
        p, q = map(int, pq.split('/'))
        j = 1
        r = []
        while p != 1 or q != 1:
            if p < q: q -= p; r.append(False)
            else: p -= q; r.append(True)
            j *= 2
        k = 1
        if p-1: r += [True]*(p-1)
        if q-1: r += [False]*(q-1)
        for t in r[::-1]:
            k *= 2
            if not t: k -= 1
        n = j - 1 + k
        ans.append(f"{i} {n}")
    print("\n".join(ans))
main()