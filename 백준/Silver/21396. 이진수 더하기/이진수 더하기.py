def main():
    t = []
    a = open(0)
    for _ in range(int(next(a))):
        c = 0
        n, x = map(int, next(a).split())
        freq = {}
        for i in map(int, next(a).split()):
            c += freq.get(i^x, 0)
            freq[i] = freq.get(i, 0) + 1
        t.append(c)
    print('\n'.join(map(str, t)))
main()