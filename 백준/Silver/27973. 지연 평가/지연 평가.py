def main():
    a = open(0)
    m = mul = 1
    add = 0
    t = []
    f = lambda x: x
    for _ in range(int(next(a))):
        x, *n = map(int, next(a).split())
        if x == 0: add += n[0]
        if x == 1: add *= n[0]; mul *= n[0]
        if x == 2: m += n[0]
        if x == 3: t.append(m * mul + add)
    print('\n'.join(map(str, t)))
main()