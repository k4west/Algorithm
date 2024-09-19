def contains(sl, s):
    for v in sl:
        if s.endswith(v):
            return True
    return False

def main():
    a = open(0)
    w = next(a).strip()
    e = int(next(a))
    sl = []
    for _ in range(e):
        if contains((wl:=next(a).strip().split()), w):
            sl.append(wl)
    t = []
    p = int(next(a))
    for _ in range(p):
        s = next(a).strip()
        flag = False
        for group in sl:
            if contains(group, s):
                flag = True
                break
        if flag:
            t.append("YES")
        else:
            t.append("NO")
    print('\n'.join(t))

if __name__ == "__main__":
    main()