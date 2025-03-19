def main():
    a = open(0)
    t = []
    for _ in range(int(next(a))):
        next(a);next(a)
        s=max(map(int, next(a).split()))
        b=max(map(int, next(a).split()))
        t.append(s<b)
    print('\n'.join(["SB"[i] for i in t]))
main()