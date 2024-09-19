def contains(sl, s):
    return any(s.endswith(v) for v in sl)

a = open(0)
w = next(a).strip()
e = int(next(a))
sl = []
for _ in range(e):
    if contains((wl:=next(a).strip().split()), w): sl.append(wl)
p = int(next(a))
for _ in range(p):
    s = next(a).strip()
    if any(map(lambda x: contains(x, s), sl)): print("YES")
    else: print("NO")