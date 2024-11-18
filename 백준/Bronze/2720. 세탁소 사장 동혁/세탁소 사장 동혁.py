a = open(0)
r = []
for _ in range(int(next(a))):
    tmp = []
    i = int(next(a))
    for c in (25, 10, 5, 1):
        tmp.append(i//c)
        i %= c
    r.append(" ".join(map(str, tmp)))
print('\n'.join(r))