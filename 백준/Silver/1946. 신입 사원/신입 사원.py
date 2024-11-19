def main():
    a = open(0)
    t = []
    for _ in range(int(next(a))):
        c = 0
        n = int(next(a))
        scores = sorted([tuple(map(int, next(a).split())) for _ in range(n)])
        m = n+1
        for _, i in scores:
            if i < m:
                c += 1
                m = i
        t.append(c)
    print('\n'.join(map(str, t)))
main()