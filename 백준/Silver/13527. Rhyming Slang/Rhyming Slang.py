def contains(sl, s):
    return any(s.endswith(v) for v in sl)

def main():
    a = open(0)
    w = next(a).strip()
    e = int(next(a))
    sl = []
    for _ in range(e):
        if contains((wl:=next(a).strip().split()), w): sl.append(wl)
    t = []
    p = int(next(a))
    for _ in range(p):
        s = next(a).strip()
        if any(map(lambda x: contains(x, s), sl)): t.append("YES")
        else: t.append("NO")
    print('\n'.join(t))

if __name__ == "__main__":
    main()