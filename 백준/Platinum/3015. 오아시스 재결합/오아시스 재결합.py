def main():
    a = iter(map(int, open(0).read().split()))
    t = 0
    s = []
    next(a)
    for i in a:
        while s and s[-1][0] < i:
            t += s.pop()[1]
        if not s:
            s.append((i, 1))
        elif s[-1][0] == i:
            j = s.pop()[1]
            t += j
            if s:
                t += 1
            s.append((i, j+1))
        else:
            s.append((i, 1))
            t += 1
    print(t)
main()