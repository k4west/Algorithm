def main():
    a = open(0)
    t = []
    for _ in range(int(next(a))):
        N, M, K = map(int, next(a).split())
        M *= K
        if N<=M:
            t.append(1)
        elif M==1:
            t.append(-1)
        else:
            c = 0
            while N > 0:
                c += 1
                N -= M
                if N > 0:
                    c += 1
                    N += 1
            t.append(c)
    print('\n'.join(map(str, t)))
main()